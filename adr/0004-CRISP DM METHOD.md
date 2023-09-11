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
In Malaysia, real estate purchase transaction are recorded by the Ministry of Finance’s Valuation and Property Service Department (or *Jabatan Penilaian dan Perkhidmatan Harta*, JPPH). JPPH charges for this data but it is provided to the public by PropertyGuru via Brickz.my website. Thus, web scraping has to be performed in order to collect the data. See the [ADR](/adr/0002-SCRAPING%20BRICKZ.md) for more info.

In addition, the data on economic indicators must also be obtained. Most of the economic indicators can be obtained from the Department of Statistics Malaysia (DOSM). See the [ADR](/adr/0003-DATA%20COLLECTION%20OF%20ECONOMIC%20INDICATORS.md) for more info.

### Data exploration
All the collected data was explored and initial evaluation was conducted based on the following question:
1. How does each dataset look like? Is it in row format or it has merged cells?
2. What is the start and end of each dataset?
3. Is the dataset from the area of interest, Kuala Lumpur?
4. How is the data quality?

### Verification of data quality
For the Transactions dataset:
- There are missing values in some columns (`built_up` and `rooms`). Need to decide to remove rows or impute.
- Values in some columns (`land_area` and `built_up`) has unit of measurement like "ft2". Need to remove.
- Values in `floors` column uses fraction instead of decimal. Need to change.
- Values in numerical columns (`land_area`, `built_up`, `price_psf` and `price`) has comma. Need to remove.
- Some values in some columns (`floors` and `rooms`) does not make sense. Need further investigation.
- Only landed properties are in the dataset. Need another round of scraping for high rise real estate.

## 3 – Data Preparation

### Data selection
The `address` column is dropped as township was used as geographical scope in this study. Precise location such as address is not needed.

## Data cleaning
The data cleaning process is as follows:
1. Change fraction in `floors` column, i.e. 1/2 to .5
2. Remove comma in `price_psf`
3. Remove comma in `price`
4. Remove comma and ft2 in `land_area` and `built_up`
5. Investigate weird `floors` values (0 and 99) and remove/impute
6. Investigate weird `rooms` values (0 and 46) and remove/impute
7. Investigate missing values in `built_up` and remove/impute
8. Investigate missing values in `rooms` and remove/impute

### Data transformation

### Data integration with external information
This dataset is integrated with economic indicators as external information, for example:
1. Overnight policy rate (interest rate) - BNM
2. Consumer price index (inflation) - DOSM
3. Household income - DOSM
4. Social wellbeing index - DOSM
5. Crime rate - DOSM
6. Population - DOSM
7. Money supply - DOSM
8. Unemployment rate - DOSM
For more information of the data collection process, see the [ADR](/adr/0003-DATA%20COLLECTION%20OF%20ECONOMIC%20INDICATORS.md) for more info.

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
