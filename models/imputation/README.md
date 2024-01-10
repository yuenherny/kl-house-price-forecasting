# Missing Value Imputation

## Experimented techniques
The techniques we experimented are:
1. Random forest
2. KNN
3. Bayesian ridge

## Features used to train the models
All columns except the target:
1. `built_up`
2. `rooms`

The `built_up` column is imputed first as it contains less missing values than `rooms`. Then the `built_up` column is included to impute the `rooms` column.
