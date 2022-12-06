import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np
import datetime
import requests

'Nazi Detector muahahaha'

with st.form(key='params_for_api'):

    speech_text = st.text_input('Input the text of your speech here to find out if you are a Nazi:', 'Your speech')
    st.form_submit_button('Make prediction')

params = dict(speech_text=speech_text)

taxifare_url = 'http://127.0.0.1:8000/predict'
response = requests.get(taxifare_url, params=params)

prediction = response.json()

pred = prediction["outcome"]

st.header(f'Are you a Nazi? - {pred}')
