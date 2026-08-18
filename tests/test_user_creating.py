import allure
from constants import StatusCodes, UserCreationMessages
from api_client import UserAPI
from data import UserCreatingData


@allure.feature('Создание пользователя')
class TestUserCreating:

    @allure.title('Создание уникального пользователя')
    @allure.description('Тест проверяет успешное создание пользователя используя уникальные генеративные данные при заполненности всех обязательных полей')
    def test_user_creating_generative_data_ok(self, creating_data_for_registration, delete_user):
        with allure.step('Создание пользователя'):
            payload = creating_data_for_registration
            create_response = UserAPI.create(payload)

            access_token = create_response.json()["accessToken"]
            delete_user.append(access_token)
        
        with allure.step('Проверка создания пользователя'):
            assert create_response.status_code == StatusCodes.OK and access_token


    @allure.title('Создание уже зарегистрированного пользователя')
    @allure.description('Тест проверяет появление ошибки при попытке создания уже зарегистрированного пользователя при заполненности всех обязательных полей')
    def test_user_creating_duplicate_data_forbidden(self, register_new_user_and_delete_and_return_data):
        with allure.step('Создание пользователя'):
            user = register_new_user_and_delete_and_return_data
            payload = user[2]

        with allure.step('Создание второго пользователя используя данные при создании первого пользователя'):
            response = UserAPI.create(payload)

        with allure.step('Проверка появления ошибки'):
            assert response.status_code == StatusCodes.FORBIDDEN and response.json() == UserCreationMessages.FORBIDDEN_EXIST


    @allure.title('Создание пользователя с незаполненным обязательным полем')
    @allure.description('Тест проверяет появление ошибки при попытке создания пользователя при незаполненности обязательного поля')
    def test_user_creating_empty_required_field_forbidden(self):
        with allure.step('Создание пользователя'):
            response = UserAPI.create(UserCreatingData.MISSING_EMAIL)

        with allure.step('Проверка появления ошибки'):
            assert response.status_code == StatusCodes.FORBIDDEN and response.json() == UserCreationMessages.FORBIDDEN_EMPTY