from datetime import datetime

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import torch
from torch.utils.data import TensorDataset
from transformers import BertTokenizer
import string
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# download our model
#### model = bucket goes here

# download BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') # downoad only once? app.state.tokenizer ?

def get_tokens(text, tokenizer, max_seq_length, add_special_tokens=True):
    """
    We have to transform the input text data into a standard format required by the
    model architecture. We define a simple get_tokens method to convert the raw text of
    our reviews to numeric values. The pretrained model accepts each observation as a
    fixed length sequence. So, if an observation is shorter than the maximum sequence
    length, then it is padded with empty (zero) tokens, and if it’s longer, then it is trunca‐
    ted. Each model architecture has a maximum sequence length that it supports. The
    tokenizer class provides a tokenize function that splits the sentence to tokens, pads
    the sentence to create the fixed-length sequence, and finally represents it as a numeri‐
    cal value that can be used during model training. This function also adds an attention
    mask to differentiate those positions where we have actual words from those that
    contain padding characters.
    """
    input_ids = tokenizer.encode(text,
                                 add_special_tokens=add_special_tokens,
                                 max_length=max_seq_length,
                                 pad_to_max_length=True)
    attention_mask = [int(id > 0) for id in input_ids]
    assert len(input_ids) == max_seq_length
    assert len(attention_mask) == max_seq_length
    return (input_ids, attention_mask)

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

    # 2 use BERT tokenizer and get tokens
    input_ids, attention_mask = get_tokens(text,tokenizer, max_seq_length=50, add_special_tokens = True)


    # 3 creation of 2 tensors: tokens, input masks (and target labels)
    input_ids_test = torch.tensor(input_ids, dtype=torch.long)
    input_mask_test = torch.tensor(attention_mask, dtype=torch.long)


    # 4 combine tensors into a tensordataset - may be DELETE
    test_dataset = TensorDataset(input_ids_test,input_mask_test)
    #test_dataset = TensorDataset(input_ids_test,input_mask_test,label_ids_test)

    return input_ids_test, input_mask_test, test_dataset



#@app.get("/predict")
#def predict(speech_text: str):

    #here the user input is turned into a dataframe so the predict function can use it
    #first speech text is the column name
 #   X_pred = pd.DataFrame(dict(
  #      speech_text=[speech_text]))
#    return dict(outcome=str("maybe"))
 #   return X_pred

@app.get("/predict")
def predict(speech_text: str):
    speech_text = preprocess_text(speech_text)[0] # inputs_ids_test
    #answer = app.state.model.predict(speech_text) # check if it returns integer, this should be the last line
    # answer = model(speech_text) #ask Elena what this line does
    answer=0

    if answer == 1:
        fr = "far right"
    else:
        fr = "not far right"
    return dict(outcome=fr)
