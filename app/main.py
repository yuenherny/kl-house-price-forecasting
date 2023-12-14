import datetime as dt
import streamlit as st

from src.about import get_about_section
from src.helpers import get_township, get_building_type, get_tenure
from src.sarimax_forecast import plot_market_overview
from src.mlp_forecast import plot_forecast_get_valuation

# st.set_page_config(layout="wide")

st.title("Real Estate Price Forecast App")

market_tab, forecast_tab, about_tab = st.tabs(["Market Overview", "Price Forecast", "About"])

with market_tab:
    st.write(
        "This app forecasts the monthly mean and median price per square feet for real estate in Kuala Lumpur."
    )
    col1, col2 = st.columns(2)

    with col1:
        in_sample_forecast_length = st.slider(
            label="In-sample forecast length",
            min_value=1,
            max_value=36,
            value=12,
        )

    with col2:
        out_sample_forecast_length = st.slider(
            label="Out-sample forecast length",
            min_value=1,
            max_value=36,
            value=12,
        )

    if st.button("SARIMAX Forecast"):
        st.plotly_chart(
            plot_market_overview(in_sample_forecast_length, out_sample_forecast_length),
            use_container_width=True,
        )


with forecast_tab:
    st.write("This app perform valuation of a real estate in Kuala Lumpur based on its attributes and economic indicators.")
    col1, col2 = st.columns(2)
    
    # Required
    with col1:
        st.subheader("Real estate attributes")
        st.write("Required. Must be provided by user.")
        township = st.selectbox(label="Select township", options=get_township())
        building_type = st.selectbox(label="Select building type", options=get_building_type())
        tenure_type = st.selectbox(label="Select tenure type", options=get_tenure())
        floors = st.slider(label="Select number of floors", min_value=1, max_value=5, value=1)
        rooms = st.slider(label="Select number of rooms", min_value=1, max_value=20, value=3)
        land_area_sqft = st.number_input(label="Enter land area (sqft)", min_value=0.0, max_value=10_000.0, value=900.0)
        built_up_sqft = st.number_input(label="Enter built-up area (sqft)", min_value=0.0, max_value=10_000.0, value=900.0)
        date = st.date_input(label="Select date", value=dt.date(2023, 7, 31))

        forecast_length = st.slider(label="Select forecast length", min_value=1, max_value=36, value=12)

        input_required = {
            'township': [township],
            'building_type': [building_type],
            'tenure': [tenure_type],
            'floors': [floors],
            'rooms': [rooms],
            'land_area': [land_area_sqft],
            'built_up': [built_up_sqft],
            'date': [date],
        }

    # Optional
    with col2:
        st.subheader("Economic indicators")
        st.write("Optional. Leave blank to use 2023 values.")
        interest_rate = st.number_input(label="Enter interest rate (%)", min_value=0.0, value=3.0)
        cpi = st.number_input(label="Enter consumer price index (2010=100)", value=123.08)
        n_households = st.number_input(label="Enter number of households", min_value=1, value=526_075)
        mean_income = st.number_input(label="Enter mean income (RM)", min_value=0.0, value=13_613.61)
        median_income = st.number_input(label="Enter median income (RM)", min_value=0.0, value=10_762.87)
        wellbeing_index = st.number_input(label="Enter wellbeing index", min_value=0.0, value=122.15)
        money_supply_millions = st.number_input(label="Enter money supply (millions)", min_value=0.0, value=2_040_993.0)
        unemployment_rate = st.number_input(label="Enter unemployment rate (%)", min_value=0.0, value=3.5)
        population_thousands = st.number_input(label="Enter population (thousands)", min_value=1.0, value=2_000.0)
        crime_rate = st.number_input(label="Enter crime rate", min_value=0, value=846)

        input_optional = {
            'cpi': [cpi],
            'median_income': [median_income],
            'mean_income': [mean_income],
            'n_households': [n_households],
            'wellbeing_index': [wellbeing_index],
            'money_supply_millions': [money_supply_millions],
            'unemployment_rate': [unemployment_rate],
            'population_thousands': [population_thousands],
            'crime_rate': [crime_rate],
            'interest_rate': [interest_rate],
        }

    if st.button("ANN Forecast"):
        figure, df_valuation = plot_forecast_get_valuation(
            input_required, input_optional, forecast_length
        )

        st.dataframe(df_valuation)

        st.plotly_chart(figure, use_container_width=True)


with about_tab:
    get_about_section()