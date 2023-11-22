
from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError
import datetime

class Form():
    def __init__(self, email=None, phone=None, date=None, text=None) -> None:
        self.email = email
        self.phone = phone
        self.date = date
        self.text = text

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        try:
            email_info = validate_email(email)
            norm_email = email_info.normalized
            self.__email = norm_email
        except (EmailNotValidError, AttributeError):
            self.__email = None
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone):
        try:
            if len(phone) == 11 and phone[0] == '7':
                self.__phone = phone
            else:
                self.__phone = None
        except TypeError:
            self.__phone = None

    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        date_format = '%Y-%m-%d'
        date_format_reverse = '%d.%m.%Y'
        try:
            date_object = datetime.datetime.strptime(date, date_format)
            self.__date = date_object.strftime('%Y-%m-%d')
        except ValueError:
            try:
                date_object_reverse = datetime.datetime.strptime(date, date_format_reverse)
                self.__date = date_object_reverse.strftime('%d.%m.%Y')
            except (ValueError, TypeError):
                self.__date = None
        except TypeError:
            self.__date = None


if __name__ == '__main__':
    form = Form('lobarev_danya@mail.ru', '79122955688', '2.12.2003', '1')
    print(form.email)
    print(form.phone)
    print(form.date)
    print(form.text)
