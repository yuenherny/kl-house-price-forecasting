# Web App Development: Real Estate Price Forecast App

Date created: 10 Dec 2023
Date revised: 16 Dec 2023

Author(s): Yu Yuen Hern

## Frameworks and Libraries
To utilise the deployment platform of Streamlit, the app is built using the Streamlit framework, with Plotly for visualisation.

For the time series forecasting, the app uses the `statsmodels` library to fit the SARIMAX model with the best order.

For machine learning, the app uses the `scikit-learn` library to fit the MLP Regressor model. MLP Regressor was chosen over Random Forest Regressor due to the storage limitation of Streamlit Share. The trained Random Forest Regressor model is too large (~1 GB) to be deployed on free version of Streamlit Share, while the trained MLP Regressor is only ~5 MB.

## Part 1: Market Overview

The plot for visualising market overview is a time series line plot of the mean and median price per square feet of transactions aggregated monthly.

This plot allows user to choose in-sample and out-sample forecast length (months ahead), and train a SARIMAX model to forecast the mean and median price per square feet of transactions for the next `n` months.

The following figures illustrate the mockup and the final look of the market overview plot:

![Mockup of Tab 1](/assets/app/tab1_mockup.png)

![Final look of Tab 1](/assets/app/tab1_webapp.png)

See the [main.py](/app/main.py) and [sarimax_forecast.py](/app/src/sarimax_forecast.py) scripts for implementation details.

## Part 2: Price Forecast

The plot for visualising price forecast is a scatter plot of the transacted price per square feet, based on the user's selection of date, township, building type, tenure type, number of floors, and land area.

This plot allows user to choose date, township, building type, tenure type, number of floors, and land area to predict the transacted price per square feet of a property. Moreover, the user can choose the forecast length (months ahead) to forecast the future value of the property, and choose to show or hide historical values of similar property in the same township.

Additionally, a dataframe above the plot illustrates the current price based on the land area and the future value of the property based on the forecasted price per square feet.

The following figures illustrate the mockup and the final look of the price forecast plot (truncated for better viewing):

![Mockup of Tab 2](/assets/app/tab2_mockup.png)

![Final look of Tab 2](/assets/app/tab2_webapp.png)

See the [main.py](/app/main.py) and [mlp_forecast.py](/app/src/mlp_forecast.py) scripts for implementation details.

## Part 3: About

This section provides a brief information about the app:
1. The author of the app
2. The motivation of the app
3. The data used to build the app and the models
4. The methodology used to build the models
5. Disclaimers