import requests 
import allure
from urls import URLs

class UserAPI:

    @staticmethod
    @allure.step(f"Создание пользователя: POST {URLs.USER_CREATION}")
    def create(payload):
        response = requests.post(URLs.USER_CREATION, json=payload, timeout=10)
        return response
    
    @staticmethod
    @allure.step(f"Авторизация пользователя: POST {URLs.USER_LOGIN}")
    def login(payload):
        response = requests.post(URLs.USER_LOGIN, json=payload, timeout=10)
        return response
    
    @staticmethod
    @allure.step(f"Удаление пользователя: DELETE {URLs.USER_DELETE}")
    def delete(payload):
        header = {"Authorization": payload}
        response = requests.delete(URLs.USER_DELETE, headers=header)
        return response
    
class OrderAPI:

    @staticmethod
    @allure.step(f"Создание заказа: POST {URLs.ORDER_CREATING}")
    def order(payload, headers=None):
        if headers is None:
            headers = {}
        response = requests.post(URLs.ORDER_CREATING, json=payload, headers=headers, timeout=10)
        return response
        