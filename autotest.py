# Качмазов М. Автотест на авторизацию по коду аторизации (https://uts.sirius.online)

import requests

URL = "https://uts.sirius.online"

LOGIN_PATH = "/smt-portal/register/login"

request_headers = {"Content-Type": "application/json"}
request_body = {"token": ""}  # шаблон тела запроса

login_code = "4602/test/8/8rr95"  # код авторизации (можно менять)

def login(login_code):  # функция для аторизации, возвращает код ответа
    request_body["token"] = login_code  # вставляет код авторизации в тело запроса
    login_response = requests.post(URL + LOGIN_PATH,
                                   json=request_body,
                                   headers=request_headers)
    return login_response.status_code


def test_login_status_code_is_200():  # проверяет код ответа
    login_status_code = login(login_code)
    assert login_status_code == 200
