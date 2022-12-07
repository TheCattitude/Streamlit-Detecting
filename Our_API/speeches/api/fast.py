from datetime import datetime

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import torch
from torch.utils.data import TensorDataset
from transformers import BertTokenizer
import string
import re
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# downloading our model
#cpu might need to be changed to gpu, trial and error
app.state.model = torch.load('https://storage.googleapis.com/eu.artifacts.speedy-surface-365113.appspot.com/containers/images/clean_model.pt', map_location='cpu')

# download BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') # downoad only once? app.state.tokenizer ?

def remove_punc(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'<[^<]+?>[^\s]+', '', text)
    text = re.sub(r'<[^<]+?>','', text)
    return text.lower()

def preprocess_text(text):
    # 1 basic cleaning
    text = remove_punc(text)

    # 2 tokenize
    tokenized = tokenizer(text, return_tensors="pt", add_special_tokens=True, max_length=50, pad_to_max_length=True)

    return tokenized


def predict_class(text):
    tokenized = preprocess_text(text)
    output_logits = model(**tokenized).logits
    preds = output_logits.detach().cpu().numpy()
    preds = np.argmax(preds, axis =1)
    return preds


@app.get("/predict")
def predict(speech_text: str):
    tokenized = preprocess_text(speech_text)
    output_logits = app.state.model(**tokenized).logits
    preds = output_logits.detach().cpu().numpy()
    preds = np.argmax(preds, axis =1)


    if preds[0] == 1:
        fr = "Yes, your text follows far-right patterns."
    else:
        fr = "No, your text could fall anywhere on the spectrum between left and conservative."
    return dict(outcome=fr)
