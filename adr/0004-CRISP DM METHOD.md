# Research Methodology: CRISP-DM Method

Date created: 4 Sep 2023
Date revised: 7 Sep 2023

Author(s): Yu Yuen Hern

## 1 – Business Understanding
More details about business understanding or problem statement can be obtained from the report. The main points are:
- Primary business objective: “Can future house prices be forecasted to determine whether a house will yield positive returns at the conclusion of its ownership period?” 
- Data mining goal: “Forecasting the future value of the house in the next three months, given the house attributes and its transacted prices.”
- Success criterion: Swanson (2015) suggests forecast with MAPE < 25% is acceptable

## 2 – Data Understanding

### Data Collection
In Malaysia, real estate purchase transaction are recorded by the Ministry of Finance’s Valuation and Property Service Department (or *Jabatan Penilaian dan Perkhidmatan Harta*, JPPH). JPPH charges for this data but it is provided to the public by PropertyGuru via Brickz.my website. Thus, web scraping has to be performed in order to collect the data. See the [ADR](/adr/0002-SCRAPING BRICKZ.md) for more info.

In addition, the data on economic indicators must also be obtained. Most of the economic indicators can be obtained from the Department of Statistics Malaysia (DOSM). See the [ADR](/adr/0003-DATA COLLECTION OF ECONOMIC INDICATORS.md) for more info.

### Data exploration
All the collected data was explored and initial evaluation was conducted based on the following question:
1. How does each dataset look like? Is it in row format or it has merged cells?
2. What is the start and end of each dataset?
3. Is the dataset from the area of interest, Kuala Lumpur?
4. How is the data quality?

#### Transactions

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
