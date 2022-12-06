from datetime import datetime
# $WIPE_BEGIN
import pandas as pd

# $WIPE_END

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# $WIPE_BEGIN
# 💡 Preload the model to accelerate the predictions
# We want to avoid loading the heavy deep-learning model from MLflow at each `get("/predict")`
# The trick is to load the model in memory when the uvicorn server starts
# Then to store the model in an `app.state.model` global variable accessible across all routes!
# This will prove very useful for demo days

#app.state.model = load_model()
# $WIPE_END

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
@app.get("/predict")
def predict(speech_text: str):


    #here the user input is turned into a dataframe so the predict function can use it
    #first speech text is the column name
    X_pred = pd.DataFrame(dict(
        speech_text=[speech_text]))

    return dict(outcome=str("maybe"))


#     model = app.state.model
#     X_processed = preprocess_features(X_pred)
#     y_pred = model.predict(X_processed)

#     # ⚠️ fastapi only accepts simple python data types as a return value
#     # among which dict, list, str, int, float, bool
#     # in order to be able to convert the api response to json
#     return dict(fare=float(y_pred))
#     # $CHA_END


# @app.get("/")
# def root():
#     # $CHA_BEGIN
#     return dict(greeting="Hello")
#     # $CHA_END
