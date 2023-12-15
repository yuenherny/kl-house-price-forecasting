import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from statsmodels.tsa.statespace.sarimax import SARIMAX

from src.helpers import get_mean_median_monthly_price_psf

mean_monthly_price_psf, median_monthly_price_psf = get_mean_median_monthly_price_psf()

mean_sarimax_best_order = (2, 2, 4)
median_sarimax_best_order = (3, 1, 1)


def _forecast_price_psf(data, order, in_sample_forecast_length=12, out_sample_forecast_length=12):

    train = data.iloc[:-in_sample_forecast_length]
    # val = data.iloc[-in_sample_forecast_length:]
    total_forecast_length = in_sample_forecast_length + out_sample_forecast_length

    model = SARIMAX(train, order=order, freq=train.index.inferred_freq)

    model = model.fit()
    model_forecast = model.get_forecast(total_forecast_length).summary_frame()

    return model_forecast['mean'], model_forecast['mean_ci_lower'], model_forecast['mean_ci_upper']


def _plot_price_psf_forecast(
    mean_monthly_price_psf, mean_forecast, mean_ci_lower, mean_ci_upper, 
    median_monthly_price_psf, median_forecast, median_ci_lower, median_ci_upper
):
    # Create Plotly figure with subplots
    fig = make_subplots(
        rows=1, cols=1, 
        subplot_titles=["Mean and Median Monthly Price PSF with Prediction Intervals in Kuala Lumpur"]
    )

    # Plot first time series and prediction interval
    fig.add_trace(go.Scatter(
        x=mean_monthly_price_psf.index, y=mean_monthly_price_psf, mode='lines', name='Mean Price PSF'
    ))
    fig.add_trace(go.Scatter(
        x=mean_forecast.index, y=mean_forecast, mode='lines', name='Forecasted Mean'
    ))
    fig.add_trace(go.Scatter(
        x=mean_forecast.index, y=mean_ci_lower, fill=None, mode='lines', line=dict(color='rgba(0,0,255,0)')
    ))
    fig.add_trace(go.Scatter(
        x=mean_forecast.index, y=mean_ci_upper, fill='tonexty', mode='lines', line=dict(color='rgba(0,0,255,0.2)'), 
        name=' Mean Price PSF Prediction Interval'
    ))

    # Plot second time series and prediction interval
    fig.add_trace(go.Scatter(
        x=median_monthly_price_psf.index, y=median_monthly_price_psf, mode='lines', name='Median Price PSF'
    ))
    fig.add_trace(go.Scatter(
        x=median_forecast.index, y=median_forecast, mode='lines', name='Forecasted Median'
    ))
    fig.add_trace(go.Scatter(
        x=median_forecast.index, y=median_ci_lower, fill=None, mode='lines', line=dict(color='rgba(255,0,0,0)')
    ))
    fig.add_trace(go.Scatter(
        x=median_forecast.index, y=median_ci_upper, fill='tonexty', mode='lines', line=dict(color='rgba(255,0,0,0.2)'), 
        name='Median Pricew PSF Prediction Interval'
    ))

    # Update layout
    fig.update_layout(
        xaxis_title="Date", 
        yaxis_title="Price per Square Feet (RM)", 
        legend_title="Legend",
    )

    return fig


def plot_market_overview(in_sample_forecast_length=12, out_sample_forecast_length=12):
    mean_forecast, mean_ci_lower, mean_ci_upper = _forecast_price_psf(
        mean_monthly_price_psf, mean_sarimax_best_order, in_sample_forecast_length, out_sample_forecast_length
    )
    median_forecast, median_ci_lower, median_ci_upper = _forecast_price_psf(
        median_monthly_price_psf, median_sarimax_best_order, in_sample_forecast_length, out_sample_forecast_length
    )
    return _plot_price_psf_forecast(
        mean_monthly_price_psf, mean_forecast, mean_ci_lower, mean_ci_upper, 
        median_monthly_price_psf, median_forecast, median_ci_lower, median_ci_upper
    )
