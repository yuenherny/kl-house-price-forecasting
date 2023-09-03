# Research Methodology: CRISP-DM Method

Date created: 4 Sep 2023
Date revised: TBD

Author(s): Yu Yuen Hern

## 1 – Business Understanding
- Primary business objective: “Can future house prices be forecasted to determine whether a house will yield positive returns at the conclusion of its ownership period?” 
- Data mining goal: “Forecasting the future value of the house in the next three months, given the house attributes and its transacted prices.”
- Success criterion: Swanson (2015) suggests forecast with MAPE < 25% is acceptable

## 2 – Data Understanding
- Data source: Transacted prices from JPPH
- Data collection: Web scraping of Brickz.my
- Data exploration
- Verification of data quality

## 3 – Data Preparation
- Data selection
- Data cleaning
- Data transformation
- Data integration with external information

## 4 – Modelling
- Classical time series: ARIMA, SARIMA, Holt’s exponential smoothing
- Machine learning: Random forest, support vector, neural networks
- Blocked cross validation

## 5 – Evaluation
- Metrics: MAE, MSE, RMSE, MAPE, R-squared
- Best model is chosen using non-parametric tests: Friedman, Iman-Davenport, Nemenyi post-hoc, similar to Zhan et al. (2023)

## 6 – Deployment
- Web app with easy-to-use UI
- Hosted on Streamlit Community Cloud
- CI/CD with GitHub-Streamlit integration
