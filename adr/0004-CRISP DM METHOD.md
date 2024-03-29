# Research Methodology: CRISP-DM Method

Date created: 4 Sep 2023

Date revised: 7 Sep 2023, 16 Dec 2023

Author(s): Yu Yuen Hern

## 1 – Business Understanding
More details about business understanding or problem statement can be obtained from the report. The main points are:
- Primary business objective: “Can future prices of a real estate be estimated for the next twelve months such that a purchase decision can be made?” 
- Data mining goal: “Forecasting the future value of a real estate for the next twelve months, given the its attributes, transacted prices and economic climate.”
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

See the [03 - Data Cleaning 1](/notebooks/03%20-%20Data%20Cleaning%201.ipynb) and [04 - Data Cleaning 2](/notebooks/04%20-%20Data%20Cleaning%202.ipynb) notebook for implementation details.

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

However, there are missing values in the economic indicators dataset. Thus, the missing values are imputed using the Time-Weighted Extrapolation method, as practiced by the United Nations (Nia, 2017).

See the [ADR](/adr/0003-DATA%20COLLECTION%20OF%20ECONOMIC%20INDICATORS.md) for more info and the [05 - Data Integration](/notebooks/05%20-%20Data%20Integration.ipynb) notebook for implementation details.

## 4 – Modelling
Upon investigation, the collected data is a panel / pooled time-series data. However, due to its complexity, we will treat it as a time series data and a normal dataset. THis gives rise to three datasets:
1. Univariate time series: Mean monthly `price_psf`
2. Univariate time series: Median monthly `price_psf`
3. Multivariate time series: The collected dataset as is and combined with other economic indicators

Based on surveyed literature, the following models performed well in real estate price forecasting:
- Classical time series: ARIMA, SARIMA, Holt’s exponential smoothing with blocked cross validation
- Machine learning: Random forest, support vector, neural networks

See [06 - Time Series Modelling](/notebooks/06%20-%20Time%20Series%20%Modelling.ipynb) and [07 - ML Modelling](/notebooks/07%20-%20ML%20Modelling.ipynb) notebooks for implementation details.

## 5 – Evaluation
Based on surveyed literature, the following nine (9) evaluation methods were selected:
1. Mean absolute error (MAE)
2. Mean squared error (MSE)
3. Root mean square error (RMSE)
4. Mean absolute percentage error (MAPE)
5. R-squared (R2)
6. Max error (ME)
7. Root mean squared log error (RMSLE)
8. Mean poisson deviation (MPD)
9. Mean gamma deviation (MGD)

The best model is chosen using the following non-parametric tests, similar to Zhan et al. (2023): 
1. Friedman test
2. Iman-Davenport test
3. Nemenyi post-hoc test

See [06 - Time Series Modelling](/notebooks/06%20-%20Time%20Series%20%Modelling.ipynb) and [07 - ML Modelling](/notebooks/07%20-%20ML%20Modelling.ipynb) notebooks for implementation details.

## 6 – Deployment
The best model from each dataset will be deployed as a web app using Streamlit framework. The Streamlit framework was chosen due to the following considerations:
1. Streamlit is a Python web app framework that is easy to use and deploy.
2. Plotly charts which are interactive is supported by Streamlit framework.
3. Python web apps can be deployed to Streamlit Community Cloud for free.
4. Streamlit Community Cloud has integration with GitHub for CI/CD.

See the [ADR](/adr/0006-WEB%20APP%20DEPLOYMENT.md) for more info, the [08 - Web App](/notebooks/08%20-Charts%20for%20Web%20App.ipynb) notebook for Plotly implementation details and the [main.py](/app/main.py) in `app` directory for web app implementation details.

## References
1. Zhan et al. (2023). A hybrid machine learning framework for forecasting house price. *Expert Systems with Applications*. Volume 233, 2023. https://doi.org/10.1016/j.eswa.2023.120981.