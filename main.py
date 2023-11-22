from typing import Union
from urllib.parse import urlparse, parse_qs
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/get_form/{query}")
def return_form_or_field(query):
    return {"all": parse_qs(query)}