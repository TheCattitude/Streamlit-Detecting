"""
taxifare model package params
load and validate the environment variables in the `.env`
"""

import os
import numpy as np

DATASET_SIZE = os.environ.get("DATASET_SIZE")
VALIDATION_DATASET_SIZE = os.environ.get("VALIDATION_DATASET_SIZE")
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE"))
LOCAL_DATA_PATH = os.path.expanduser(os.environ.get("LOCAL_DATA_PATH"))
LOCAL_REGISTRY_PATH = os.path.expanduser(os.environ.get("LOCAL_REGISTRY_PATH"))
PROJECT = os.environ.get("PROJECT")
DATASET = os.environ.get("DATASET")

# Use this to optimize loading of raw_data with headers: pd.read_csv(..., dtypes=..., headers=True)
DTYPES_RAW_OPTIMIZED = {
    "key": "O",
    "fare_amount": "float32",
    "pickup_datetime": "O",
    "pickup_longitude": "float32",
    "pickup_latitude": "float32",
    "dropoff_longitude": "float32",
    "dropoff_latitude": "float32",
    "passenger_count": "int8"
}

COLUMN_NAMES_RAW = DTYPES_RAW_OPTIMIZED.keys()

# Use this to optimize loading of raw_data without headers: pd.read_csv(..., dtypes=..., headers=False)
DTYPES_RAW_OPTIMIZED_HEADLESS = {
    0: "O",
    1: "float32",
    2: "O",
    3: "float32",
    4: "float32",
    5: "float32",
    6: "float32",
    7: "int8"
}

DTYPES_PROCESSED_OPTIMIZED = np.float32



################## VALIDATIONS #################

env_valid_options = dict(
    DATASET_SIZE=["1k", "10k", "100k", "500k", "50M", "new"],
    VALIDATION_DATASET_SIZE=["1k", "10k", "100k", "500k", "500k", "new"],
    DATA_SOURCE=["local", "big query"],
    MODEL_TARGET=["local", "gcs", "mlflow"],
    PREFECT_BACKEND=["development", "production"],
)

def validate_env_value(env, valid_options):
    env_value = os.environ[env]
    if env_value not in valid_options:
        raise NameError(f"Invalid value for {env} in `.env` file: {env_value} must be in {valid_options}")


for env, valid_options in env_valid_options.items():
    validate_env_value(env, valid_options)
