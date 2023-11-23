from typing import Union
from urllib.parse import urlparse, parse_qs
from fastapi import FastAPI
from db import checkQueryDB
from formchecker import Form, emailValidator, phoneValidator, dateValidator
from tinydb import TinyDB, Query

app = FastAPI()

# Функция, принимающая post запрос с query параметрами

@app.post("/get_form/{query}")
def return_form_or_field(query):
    query_parse = parse_qs(query)
    FormCheck = Form()
    
    if 'email' in query_parse:
        if emailValidator(query_parse['email'][0]):
            FormCheck.email = query_parse['email'][0]
            query_parse['email'] = 'EmaiField'
        else:
            query_parse['email'] = 'NoneField'

    if 'phone' in query_parse:
        if phoneValidator(query_parse['phone'][0]):
            FormCheck.phone = query_parse['phone'][0]
            query_parse['phone'] = 'PhoneField'
        else:
            query_parse['phone'] = 'NoneField'
            
    if 'date' in query_parse:
        if dateValidator(query_parse['date'][0]):
            FormCheck.date = query_parse['date'][0]
            query_parse['date'] = 'DateField'
        else:
            query_parse['date'] = 'NoneField'
    
    if 'text' in query_parse:
        FormCheck.text = query_parse['text'][0]
        query_parse['text'] = 'TextField'

    standart_queries = ['email', 'phone', 'date', 'text']

    for key, value in query_parse.items():
        if key not in standart_queries:
            query_parse[key] = 'NoneField'

    num_of_table = checkQueryDB(FormCheck)

    if num_of_table is not None:
        return {"template name": num_of_table}
    else: 
        return query_parse