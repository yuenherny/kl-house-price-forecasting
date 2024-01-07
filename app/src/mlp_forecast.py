import datetime as dt
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from src.helpers import (
    MODEL_DIR, get_encoder, get_model, get_scaler, get_transactions, get_mean_median_monthly_price_psf,
    get_months_difference
)

encoder_path = MODEL_DIR / 'one_hot_encoder_township_building_type_tenure.joblib'
scaler_path = MODEL_DIR / 'mlp_forecasting_scaler.skops'
model_path = MODEL_DIR / 'mlp_10_lr001_iter100_forecasting.skops'

df_transactions = get_transactions()
mean_monthly_price_psf, median_monthly_price_psf = get_mean_median_monthly_price_psf()
data_cutoff_date = dt.datetime(2023, 6, 30)


def _process_dataframe(df_input_required: pd.DataFrame):

    df_input_required['township'] = df_input_required['township'].astype('category')
    df_input_required['building_type'] = df_input_required['building_type'].astype('category')
    df_input_required['tenure'] = df_input_required['tenure'].astype('category')
    df_input_required['date'] = pd.to_datetime(df_input_required['date'], yearfirst=True)
    df_input_required['year'] = df_input_required['date'].dt.year
    df_input_required['month'] = df_input_required['date'].dt.month
    df_input_required['day'] = df_input_required['date'].dt.day

    return df_input_required


def _expand_forecast_horizon(df_input_required: pd.DataFrame, forecast_length=12):
    start_date = df_input_required['date'].iloc[0]
    months_difference = get_months_difference(data_cutoff_date, start_date)
    forecast_length += months_difference

    df_input_required = pd.concat([df_input_required] * forecast_length)
    df_input_required['date'] = pd.date_range(start=data_cutoff_date, periods=forecast_length, freq='MS')
    return df_input_required, months_difference


def _encode_dataframe(df_input_required: pd.DataFrame, input_optional: dict):

    ohe = get_encoder(encoder_path)
    df_encoded = ohe.transform(df_input_required.drop(columns=['date']))

    df_input = pd.concat([pd.DataFrame({**input_optional}), df_encoded], axis=1)
    return df_input.drop(columns=['land_area']), df_input_required


def _forecast_price_psf(df_input: pd.DataFrame):

    scaler = get_scaler(scaler_path)
    input_scaled = scaler.transform(df_input.to_numpy())

    model = get_model(model_path)
    return model.predict(input_scaled)


def _plot_price_psf_forecast(combined_df, mean_monthly_price_psf, median_monthly_price_psf):

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    color_map = {'Historical': '#EF553B', 'Current': '#636EFA', 'Future': '#00CC96'}
    # Create a scatter plot with Plotly

    for type in combined_df['type'].unique():
        subset_df = combined_df[combined_df['type'] == type]
        fig.add_trace(
            go.Scatter(
                x=subset_df['date'], 
                y=subset_df['price_psf'],
                mode='markers', 
                marker=dict(color=color_map[type]),
                name=f'{type}'
            )
        )

    # Line plot for mean price
    fig.add_trace(
        go.Scatter(
            x=mean_monthly_price_psf.index, 
            y=mean_monthly_price_psf.values,
            mode='lines', 
            line=dict(color='black'), 
            name='Mean Price'
        ), 
        secondary_y=True
    )

    # Line plot for median price
    fig.add_trace(
        go.Scatter(
            x=median_monthly_price_psf.index, 
            y=median_monthly_price_psf.values,
            mode='lines', 
            line=dict(color='purple'), 
            name='Median Price'
        ),
        secondary_y=True
    )

    # Set labels and title
    fig.update_layout(
        title='Price per Square Foot (PSF) of Selected Township with Kuala Lumpur Mean and Median PSF over Time ',
        xaxis_title='Date',
        yaxis_title='Price per Square Foot',
        yaxis=dict(matches='y2'), 
        yaxis2=dict(matches='y'),
        legend=dict(
            title="Legend",
            orientation="h",
            yanchor="top",
            xanchor="left",
            x=0,
            y=-0.2,
        )
    )

    # Set x-axis limits based on the first and last date in combined_df
    first_date = combined_df['date'].min()
    last_date = combined_df['date'].max()
    fig.update_xaxes(range=[first_date, last_date])

    return fig


def _combine_historical_and_forecast(df_input_required: pd.DataFrame, forecast, months_difference, show_similar: bool):

    township = df_input_required['township'].iloc[0]
    df_historical = df_transactions.query(f"township == '{township}'")
    
    if show_similar:  # Show only historical transactions of similar attributes
        building_type = df_input_required['building_type'].iloc[0]
        tenure = df_input_required['tenure'].iloc[0]
        rooms = df_input_required['rooms'].iloc[0]
        floors = df_input_required['floors'].iloc[0]

        df_historical = df_transactions.query(
            f"township == '{township}' and building_type == '{building_type}' and tenure == '{tenure}' and rooms == {rooms} and floors == {floors}"
        )
    
    df_historical = df_historical[['date', 'price_psf']]
    df_historical['type'] = 'Historical'

    df_forecast = pd.DataFrame({'date': df_input_required['date'], 'price_psf': forecast}).reset_index(drop=True)
    df_forecast.loc[:months_difference + 1, 'type'] = 'Current'

    if len(df_forecast) > 1:
        df_forecast.loc[1:, 'type'] = 'Future'

    combined_df = pd.concat([df_historical, df_forecast], ignore_index=True)

    return combined_df


def _create_valuation_df(df_input_required, forecast):
    df_forecast = pd.DataFrame({'Date': df_input_required['date'], 'Price per square feet (RM)': forecast}).reset_index(drop=True)
    df_forecast['Date'] = df_forecast['Date'].dt.date
    df_forecast['Valuation using Built-up Area (RM)'] = df_forecast['Price per square feet (RM)'] * df_input_required['built_up'].iloc[0]
    df_forecast['Valuation using Land area (RM)'] = df_forecast['Price per square feet (RM)'] * df_input_required['land_area'].iloc[0]
    return df_forecast


def plot_forecast_get_valuation(input_required: dict, input_optional: dict, forecast_length: int, show_similar: bool):
    
    df_input_required = pd.DataFrame({**input_required})
    df_input_required, months_difference = _expand_forecast_horizon(df_input_required, forecast_length)

    df_input_required = _process_dataframe(df_input_required)
    df_input, df_input_required = _encode_dataframe(df_input_required, input_optional)
    forecast = _forecast_price_psf(df_input)

    df_valuation = _create_valuation_df(df_input_required, forecast)
    combined_df = _combine_historical_and_forecast(df_input_required, forecast, months_difference, show_similar)

    figure = _plot_price_psf_forecast(combined_df, mean_monthly_price_psf, median_monthly_price_psf)
    df_valuation = _create_valuation_df(df_input_required, forecast)

    return figure, df_valuation
