import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests

'Nazi Detector muahahaha'

with st.form(key='params_for_api'):

    speech_text = st.text_input('Input the text of your speech here to find out if you are a Nazi:')
    st.form_submit_button('Make prediction')

params = dict(speech_text=speech_text)

speeches_url = 'https://speeches-t3lqethc6a-ew.a.run.app/predict'
response = requests.get(speeches_url, params=params)

prediction = response.json()

pred = prediction["outcome"]

st.header(f'Are you a Nazi? - {pred}')
