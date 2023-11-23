from tinydb import TinyDB, Query
from formchecker import Form

# Работа с базой

def checkQueryDB(form):

    db = TinyDB('tables/db.json')
    Form_queries = Query()
    dict_form_orig = {'email': form.email, 'phone': form.phone, 'date': form.date, 'text': form.text}

    dict_form = {}
    for key, value in dict_form_orig.items():
        if value is not None:
            dict_form[key] = value

    for key, value in dict_form.items():
    # Создаем запрос к таблице для поиска элемента с заданным ключом и значением
        result = db.search(Form_queries[key] == value)
        if not result:
            print(f"Элемент с ключом '{key}' и значением '{value}' не найден в таблице")
    
    # На случай, если все query = None
    try:
        for t in result:
            for key, value in dict_form.items():
                if key in t and t[key] == value:
                    pass
                else:
                    result.remove(t)
    except UnboundLocalError:
        result = []
                
    if len(result) > 0:
        return result[0].doc_id
    else:
        return None

if __name__ == '__main__':
    form = Form(phone='7912295568')
    print(checkQueryDB(form))