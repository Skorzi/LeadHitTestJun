from typing import Union
from urllib.parse import urlparse, parse_qs
from fastapi import FastAPI
from db import checkQueryDB
from formchecker import Form
from tinydb import TinyDB, Query

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
    FormCheck = Form()
    
    if 'email' in query_parse:
        FormCheck.email = query_parse['email'][0]
    
    if 'phone' in query_parse:
        FormCheck.phone = query_parse['phone'][0]
    
    if 'date' in query_parse:
        FormCheck.date = query_parse['date'][0]
    
    if 'text' in query_parse:
        FormCheck.text = query_parse['text'][0]
    
    num_of_table = checkQueryDB(FormCheck)
    
    return {"template name": num_of_table}