import pytest
import generators
from api_client import UserAPI, OrderAPI

@pytest.fixture(scope='function')
def register_new_user_and_delete_and_return_data():

    email = f"test-data{generators.generate_random_string(7)}@yandex.ru"
    password = generators.generate_random_string(7)
    name = generators.generate_random_string(7)


    create_payload = {
        "email": email,
        "password": password,
        "name": name
    }

    create_result = UserAPI.create(create_payload)

    assert create_result.status_code == 200, f'Регистрация не удалась: {create_result.text}'

    response_json = create_result.json()
    access_token = response_json.get("accessToken")

    yield create_result.status_code, create_result.json(), create_payload, email, password

    delete_result = UserAPI.delete(access_token)

    assert delete_result.status_code in [200, 202], f'Удаление не удалось: {delete_result.text}'

    print(f"Пользователь удалён, статус: {delete_result.status_code}")



@pytest.fixture(scope='function')
def autharization_user_and_return_data(register_new_user_and_delete_and_return_data):

    email = register_new_user_and_delete_and_return_data[3]
    password = register_new_user_and_delete_and_return_data[4]

    login_payload = {
        "email": email,
        "password": password
    }

    auth_result = UserAPI.login(login_payload)

    assert auth_result.status_code == 200, f'Авторизация не удалась: {auth_result.text}'

    response_json = auth_result.json()
    access_token = response_json.get("accessToken") 

    yield auth_result.status_code, auth_result.json(), login_payload, access_token
    

