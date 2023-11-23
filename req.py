import requests

def main():
    data = requests.post('http://127.0.0.1:8000/get_form/email=la@mail.ru&phone=79122955688&date=02.02.2003', '')
    print(data.content)

    data = requests.post('http://127.0.0.1:8000/get_form/email=la@mail.ru&phone=79122955688', '')
    print(data.content)

    data = requests.post('http://127.0.0.1:8000/get_form/phone=79122955688', '')
    print(data.content)

    data = requests.post('http://127.0.0.1:8000/get_form/email=lobarev@mail.ru&phone=79122955688&test=quas98', '')
    print(data.content)

if __name__ == '__main__':
    main()