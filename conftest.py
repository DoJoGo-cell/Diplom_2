import pytest
import allure
import generators
from api_client import UserAPI

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

    response_json = create_result.json()
    access_token = response_json.get("accessToken")

    yield create_result.status_code, create_result.json(), create_payload, email, password

    delete_result = UserAPI.delete(access_token)
    allure.attach(
        f"Пользователь удалён, статус: {delete_result.status_code}",
        name="Cleanup: удаление пользователя",
        attachment_type=allure.attachment_type.TEXT
    )

@pytest.fixture(scope='function')
def autharization_user_and_return_data(register_new_user_and_delete_and_return_data):

    email = register_new_user_and_delete_and_return_data[3]
    password = register_new_user_and_delete_and_return_data[4]

    login_payload = {
        "email": email,
        "password": password
    }

    auth_result = UserAPI.login(login_payload)

    response_json = auth_result.json()
    access_token = response_json.get("accessToken") 

    return auth_result.status_code, auth_result.json(), login_payload, access_token

@pytest.fixture(scope='function')
def creating_data_for_registration():
    
    email = f"test-data{generators.generate_random_string(7)}@yandex.ru"
    password = generators.generate_random_string(7)
    name = generators.generate_random_string(7)


    create_payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return create_payload

@pytest.fixture(scope='function')
def delete_user():

    tokens = []

    yield tokens

    for token in tokens:
        delete_result = UserAPI.delete(token)
        allure.attach(
            f"Пользователь удалён, статус: {delete_result.status_code}",
            name="Cleanup: удаление пользователя",
            attachment_type=allure.attachment_type.TEXT
        )
