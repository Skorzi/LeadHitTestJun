import requests


def main():
    data = requests.post('http://127.0.0.1:8000/get_form/f_name1=value1&f_name2=value2', '')
    print(data.content)
if __name__ == '__main__':
    main()