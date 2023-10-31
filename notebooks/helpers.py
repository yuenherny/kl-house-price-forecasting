"""Helper functions for notebooks."""
import os
from pathlib import Path

import re
from math import sqrt
import pandas as pd
import numpy as np

from sklearn.exceptions import NotFittedError
from sklearn.metrics import (
    accuracy_score, balanced_accuracy_score, f1_score, precision_score, recall_score,
    median_absolute_error, mean_absolute_error, mean_absolute_percentage_error, mean_squared_error,
    r2_score
)
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline

ROOT_DIR = Path(os.getcwd()).parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
TRANSFORMED_DATA_DIR = DATA_DIR / 'transformed'
CACHE_DATA_DIR = DATA_DIR / 'cache'

ASSETS_DIR = ROOT_DIR / 'assets'
CHARTS_DIR = ASSETS_DIR / 'plotly'

MODELS_DIR = ROOT_DIR / 'models'
OUTLIER_MODEL_DIR = MODELS_DIR / 'outlier_detection'
ENCODER_MODEL_DIR = MODELS_DIR / 'encoding'
FORECAST_MODEL_DIR = MODELS_DIR / 'forecasting'
IMPUTER_MODEL_DIR = MODELS_DIR / 'imputation'
SCALER_MODEL_DIR = MODELS_DIR / 'scaling'

def convert_mixed_fraction_to_decimal(value):
    """Convert a mixed fraction to a decimal."""
    match = re.match(r'(\d+)½', value)
    if match:
        whole_part = float(match.group(1))
        fractional_part = 0.5  # Since ½ represents 1/2
        return whole_part + fractional_part

    match = re.match(r'(\d+)¾', value)
    if match:
        whole_part = float(match.group(1))
        fractional_part = 0.75  # Since ¾ represents 3/4
        return whole_part + fractional_part

    match = re.match(r'(\d+)⅖', value)
    if match:
        whole_part = float(match.group(1))
        fractional_part = 0.4  # Since ⅖ represents 2/5
        return whole_part + fractional_part

    # Return 0 for cases where the format doesn't match
    return value


def validate_impute(y_val: pd.Series, y_val_pred: np.ndarray, task: str = 'regression'):
    """Function to validate imputation models."""

    print("Results for validation set:")
    if task == 'regression':
        print(f"R2 score: {r2_score(y_val, y_val_pred)}")
        print(f"RMSE score: {sqrt(mean_squared_error(y_val, y_val_pred))}")
        print(f"MAPE score: {mean_absolute_percentage_error(y_val, y_val_pred)}")
        print(f"MAE score: {mean_absolute_error(y_val, y_val_pred)}")
        print(f"Median AE score: {median_absolute_error(y_val, y_val_pred)}")
    elif task == 'classification':
        print(f"Accuracy score: {accuracy_score(y_val, y_val_pred)}")
        print(f"Balanced accuracy score: {balanced_accuracy_score(y_val, y_val_pred)}")
        print(f"Macro F1 score: {f1_score(y_val, y_val_pred, average='macro')}")
        print(f"Weighted F1 score: {f1_score(y_val, y_val_pred, average='weighted')}")
        print(f"Macro precision score: {precision_score(y_val, y_val_pred, average='macro')}")
        print(f"Weighted precision score: {precision_score(y_val, y_val_pred, average='weighted')}")
        print(f"Macro recall score: {recall_score(y_val, y_val_pred, average='macro')}")
        print(f"Weighted recall score: {recall_score(y_val, y_val_pred, average='weighted')}")


def cross_validation_with_pipeline(pipeline: Pipeline, X_train: np.ndarray, y_train: np.ndarray, task: str):
    """Function to perform cross validation with a pipeline."""

    # Cross validate the train data
    if task == 'regression':
        scoring = ('r2', 'neg_root_mean_squared_error', 'neg_mean_absolute_percentage_error', 'neg_median_absolute_error')
    elif task == 'classification':
        scoring = ('accuracy', 'balanced_accuracy', 'f1', 'precision', 'recall', 'roc_auc')
    else:
        scoring = None

    cv_results = cross_validate(pipeline, X_train, y_train, cv=5, scoring=scoring, return_train_score=True, n_jobs=4)
    
    return cv_results


def train_and_validate_model(pipeline: Pipeline, X_train: pd.Series, y_train: pd.Series, X_val: pd.Series, y_val: pd.Series, task: str):
    """Function to train and validate a model."""

    try:
        y_pred = pipeline.predict(X_val)
    except NotFittedError:
        print('Pipeline not fitted. Start training...')
        pipeline = pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_val)

    validate_impute(y_val, y_pred, task)

    return pipeline
