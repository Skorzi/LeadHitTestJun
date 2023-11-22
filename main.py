from typing import Union
from urllib.parse import urlparse, parse_qs
from fastapi import FastAPI
from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError
from formchecker import Form

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/get_form/{query}")
def return_form_or_field(query):
    query_parse = parse_qs(query)
    form_for_check = Form()
    
    if 'email' in query_parse:
        form_for_check.email = query_parse['email'][0]
    
    if 'phone' in query_parse:
        form_for_check.phone = query_parse['phone'][0]
    
    if 'date' in query_parse:
        form_for_check.date = query_parse['date'][0]
    
    if 'text' in query_parse:
        form_for_check.text = query_parse['text'][0]
    
    return {"all": [form_for_check.email, form_for_check.phone, form_for_check.date, form_for_check.text]}