import streamlit as st
import pandas as pd
import numpy as np
import datetime
import requests

st.title('Does your speech text follow far-right patterns?')

with st.form(key='params_for_api'):

    speech_text = st.text_input('Input your speech here:')
    submit_button = st.form_submit_button('Make prediction')

params = dict(speech_text=speech_text)


speeches_url = 'https://speechesv2-t3lqethc6a-ew.a.run.app/predict'
#speeches_url = 'http://localhost:8000/predict'

response = requests.get(speeches_url, params=params)

prediction = response.json()

pred = prediction["outcome"]

st.header('At an accuracy of 82% your speech is:')

if submit_button:
    st.header(pred)
