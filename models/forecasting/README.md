# Forecasting with machine learning

## Experimented models
The models we experimented are:
1. Random forest
2. Support vector regression
3. Neural networks

## Features used to train the models
All columns except the target:
1. `price_psf`
2. `price`

## Evaluation metrics
1. Mean absolute error (MAE)
2. Mean squared error (MSE)
3. Root mean squared error (RMSE)
4. Mean absolute percentage error (MAPE)
5. R-squared (R2)
6. Max error (ME)
7. Root mean squared log error (RMSLE)
8. Mean poisson deviance (MPD)
9. Mean gamma deviance (MGD)

## Selection of best model
The best model is selected based on the lowest average rank of the evaluation metrics and statistical tests:
1. Friedman test
2. Nemenyi post-hoc test
