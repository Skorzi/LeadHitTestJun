
from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError
import datetime

def emailValidator(email):
    try:
        validate_email(email)
        return True
    except (EmailNotValidError, AttributeError):
        return False

def phoneValidator(phone):
    try:
        if len(phone) == 11 and phone[0] == '7':
            return True
        else:
            return False
    except TypeError:
        return False

def dateValidator(date):
    date_format = '%Y-%m-%d'
    date_format_reverse = '%d.%m.%Y'
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except ValueError:
        try:
            datetime.datetime.strptime(date, date_format_reverse)
            return True
        except (ValueError, TypeError):
            return False
    except TypeError:
        return False

class Form():
    def __init__(self, email=None, phone=None, date=None, text=None) -> None:
        self.email = email
        self.phone = phone
        self.date = date
        self.text = text

    def createTypeField():
        pass


if __name__ == '__main__':
    form = Form('lobarev_danya@mail.ru', '79122955689', '2.12.2003', '1')
    print(form.email)
    print(form.phone)
    print(form.date)
    print(form.text)
