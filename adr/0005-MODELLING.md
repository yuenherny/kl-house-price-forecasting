# Modelling: Time Series Forecasting of Real Estate Prices

Date created: 16 Nov 2023
Date revised: 16 Dec 2023

Author(s): Yu Yuen Hern

## Data Type
Data associated with forecasting can be categorised into several types:
1. Time series data: One observation per timestamp, collected at regular intervals over time (Hyndman & Athanasopoulos, 2018)
2. Cross-sectional data: One observation per entity, collected at the same point in time (Hyndman & Athanasopoulos, 2018)
3. Panel / pooled data: One observation per entity, collected at multiple points in time (Dielman, 1983)

The collected data from Brickz.my is a collection of purchase transactions of real estate, with transaction date as time element. As there are no limitations of the number of transactions per day, each timestamp can have more than one data point.

Each transaction is a cross-sectional data containing other external features which could impact price per square feet. Moreover, the data is collected at different points in time. Thus, it is a panel / pooled data.

However, due to the complexity of panel / pooled data, the data will be simplified to a time series data. The data will be aggregated by month, and the price per square feet will be averaged. The external features will be ignored for for time series modelling but will be used for machine learning modelling.

## Time Series Modelling

### Data Splitting
Dataset is split into training and testing based on the year attribute, where:
- Training and validation set: Year 2000 to 2020
- Testing set: Year 2021 to 2023
as we want to use historical values to forecast future values.

### Data Transformation
Due to the presence of external features, the data needs to be simplified. The following aggregation methods were considered:
1. Aggregated yearly for mean and median
2. Aggregated monthly for mean and median
3. Aggregated daily for mean and median

The following was observed for all three methods:
1. Too little data points for yearly aggregation
2. Too much data points for daily aggregation, and the data is too volatile and noisy
3. Monthly aggregation has the right amount of data points (232), and the data is less volatile and noisy
Thus, the data is aggregated monthly for mean and median for time series modelling. However, the dataset is used as is for machine learning modelling.

### Grid Search with Blocked Cross Validation
Pirbazari et al. (2021) suggested the use of blocked cross validation for time series data. Blocked cross validation is quite similar to K-Fold, where the data (not shuffled) is split into blocks, and a small portion in the block is used as validation set. This method is used to prevent data leakage, as the data is time dependent. The following figure illustrates the blocked cross validation method (Pirbazari et al., 2021).

![Blocked Cross Validation](/assets/adr/blocked_cv.png)

### Model Evaluation on Test Set
Similar to Zhan et al. (2023), the following metrics were used to evaluate the model performance:
1. Mean absolute error (MAE)
2. Mean squared error (MSE)
3. Root mean square error (RMSE)
4. Mean absolute percentage error (MAPE)
5. R-squared (R2)
6. Max error (ME)
7. Root mean squared log error (RMSLE)
8. Mean poisson deviation (MPD)
9. Mean gamma deviation (MGD)

However, we cannot just use a single metric for selecting the best model. Thus, we will use non-parametric tests to select the best model, as suggested by Zhan et al. (2023).

### Statistical Evaluation of Model Performance
In order to select the best model, non-parametric tests are used to compare the performance of the models. The following tests are used:
1. Friedman test: Tests the null hypothesis that all models have the same performance.
2. Iman-Davenport test: Tests the null hypothesis that all models have the same performance, when there is a large number of evaluation metrics.
3. Nemenyi post-hoc test: Finds out which models are significantly better than the other.

These models rely on the mean rank of the models, which is calculated from the rank of each model on each evaluation metric, and not the actual values. See [06 - Time Series Modelling](/notebooks/06%20-%20Time%20Series%20%Modelling.ipynb) notebook for implementation details.

## Machine Learning Modelling

### Data Splitting
Similar to time series modelling, the dataset is split into training and testing based on the year attribute.

### Data Transformation
Contrary from time series modelling, the data is not aggregated, and the external features are included.

However, machine learning models are unable to handle non-numeric features. One hot encoding is used to convert the non-numeric features into numeric features. Then the features are scaled using the standard scaler.

### Grid Search with K-Fold Cross Validation
Based on surveyed literature, the following models were considered:
1. Random forest regressor (RandomForestRegressor)
2. Support vector regressor (SVR)
3. Mutilayer perceptron regressor (MLPRegressor)
where the hyperparameters from the literature were used as reference values to select the candidate hyperparameters for grid search.

By default, the GridSearchCV uses K-Fold cross validation. However due to the large size of the dataset, it keeps running into memory issue. Thus learning curve was fitted to each candidate model to determine the best sample size for cross validation, as suggested by Melvin (2021).

### Model Evaluation on Test Set
Similar evaluation metrics for time series modelling were used for machine learning modelling.

### Statistical Evaluation of Model Performance
Similar statistical tests for time series modelling were used for machine learning modelling.

See [07 - ML Modelling](/notebooks/07%20-%20ML%20Modelling.ipynb) notebook for implementation details.

# References
1. Dielman, 1983: https://www.jstor.org/stable/2685870
2. Hyndman & Athanasopoulos, 2018: https://otexts.com/fpp2/data-methods.html#data-methods
3. Melvin, 2021: https://sites.uab.edu/periop-datascience/2021/06/28/sample-size-in-machine-learning-and-artificial-intelligence/