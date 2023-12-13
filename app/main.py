import streamlit as st

from src.about import get_about_section
from src.sarimax_forecast import plot_market_overview

st.title("Real Estate Price Forecast App")

market_tab, forecast_tab, about_tab = st.tabs(["Market Overview", "Price Forecast", "About"])

with market_tab:
    st.write(
        "This app forecasts the monthly mean and median price per square feet for real estate in Kuala Lumpur."
    )

    in_sample_forecast_length = st.slider(
        label="In-sample forecast length",
        min_value=1,
        max_value=36,
        value=12,
    )

    out_sample_forecast_length = st.slider(
        label="Out-sample forecast length",
        min_value=1,
        max_value=36,
        value=12,
    )

    if st.button("Forecast"):
        st.plotly_chart(
            plot_market_overview(in_sample_forecast_length, out_sample_forecast_length),
            use_container_width=True,
        )


with about_tab:
    get_about_section()