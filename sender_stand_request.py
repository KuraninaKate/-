import data
import configuration
import requests


# Документация
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


# Создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_MAIN_USER,
                         json=body,
                         headers=data.headers)


# Авторизация
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")


# Создание набора
def post_new_kit(kit_body, token):
    new_headers = data.headers.copy()
    new_headers["Authorization"] = f"Baerer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_MAIN_KITS,
                         json=kit_body,
                         headers=data.headers)

