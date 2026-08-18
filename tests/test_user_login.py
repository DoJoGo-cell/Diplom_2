import allure
from constants import StatusCodes, UserLoginMessages
from api_client import UserAPI
from data import UserLoginData


@allure.feature('Авторизация пользователя')
class TestUserLogin:

    @allure.title('Авторизация существующего пользователя')
    @allure.description('Тест проверяет успешную авторизация существующего пользователя')
    def test_user_login_registered_user_ok(self, autharization_user_and_return_data):
        with allure.step('Авторизация курьера'):
            user = autharization_user_and_return_data
            status_code = user[0]
            response = user[1]

        with allure.step('Проверка авторизации пользователя'):
            assert status_code == StatusCodes.OK and response["accessToken"]

    @allure.title('Авторизация пользователя используя неверный логин и пароль')
    @allure.description('Тест проверяет появление ошибки при авторизация пользователя используя неверный логин и пароль')
    def test_user_login_invalid_data_unauthorized(self):
        with allure.step('Авторизация курьера'):
            response = UserAPI.login(UserLoginData.INVALID_DATA)

        with allure.step('Проверка авторизации пользователя'):
            assert response.status_code == StatusCodes.UNAUTHORIZED and response.json() == UserLoginMessages.UNAUTHORIZED

