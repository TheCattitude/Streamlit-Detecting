import pickle
import pandas as pd
import os
import pytest
import numpy as np

from taxifare.ml_logic.params import DTYPES_RAW_OPTIMIZED


@pytest.fixture(scope="session")  # cached fixture
def train_1k()->pd.DataFrame:

    gcs_path = "https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/train_1k.csv"
    df_raw = pd.read_csv(gcs_path, dtype=DTYPES_RAW_OPTIMIZED)

    return df_raw


@pytest.fixture(scope='session')
def train_1k_cleaned()->pd.DataFrame:
    gcs_path = "https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/solutions/train_1k_cleaned.csv"
    df_cleaned = pd.read_csv(gcs_path, dtype=DTYPES_RAW_OPTIMIZED)

    return df_cleaned


@pytest.fixture(scope='session')
def X_processed_1k() -> np.ndarray:
    with open(os.path.join(os.path.dirname(__file__), "fixtures", "X_processed_1k.npy"), "rb") as f:
        X_processed_1k = np.load(f)
    return X_processed_1k


@pytest.fixture(scope='session')
def y_1k() -> pd.Series:
    with open(os.path.join(os.path.dirname(__file__), "fixtures", "y_1k.npy"), "rb") as f:
        y = np.load(f)
    return y
