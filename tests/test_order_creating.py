import allure
from constants import StatusCodes
from api_client import OrderAPI
from data import OrderCreatingData


@allure.feature('Создание заказа')
class TestOrderCreating:

    @allure.title('Создание заказа с авторизацией')
    @allure.description('Тест проверяет успешное создание заказа при авторизированном пользователе с ингредиентами')
    def test_order_creating_with_auth_ok(self, autharization_user_and_return_data):
        with allure.step('Создание заказа'):
            access_token = autharization_user_and_return_data[3]
            headers = {"Authorization": access_token}
            response = OrderAPI.order(OrderCreatingData.BURGER_WITH_INGREDIENTS, headers=headers)

        with allure.step('Проверка создания заказа'):
            assert response.status_code == StatusCodes.OK and response.json().get("success") is True

    @allure.title('Создание заказа без авторизации')
    @allure.description('Тест проверяет попытку создания заказа при не авторизированном пользователе')
    def test_order_creating_without_auth_error(self, ):
        with allure.step('Создание заказа'):
            response = OrderAPI.order(OrderCreatingData.BURGER_WITH_INGREDIENTS)

        with allure.step('Проверка появления ошибки'):
            assert response.status_code != StatusCodes.OK, f'Заказ был создан, статус - {response.status_code}'

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Тест проверяет попытку создания заказа без ингридиентов при авторизированном пользователе')
    def test_order_creating_without_ingredients_bad_request(self, autharization_user_and_return_data):
        with allure.step('Создание заказа'):
            access_token = autharization_user_and_return_data[3]
            headers = {"Authorization": access_token}
            response = OrderAPI.order(OrderCreatingData.BURGER_WITHOUT_INGREDIENTS, headers=headers)

        with allure.step('Проверка создания заказа'):
            assert response.status_code == StatusCodes.BAD_REQUEST

    @allure.title('Создание заказа c неверным хэшем ингредиентов')
    @allure.description('Тест проверяет попытку создания заказа c неверным хэшем ингридиентов при авторизированном пользователе')
    def test_order_creating_invalid_href_internal_server_error(self, autharization_user_and_return_data):
        with allure.step('Создание заказа'):
            access_token = autharization_user_and_return_data[3]
            headers = {"Authorization": access_token}
            response = OrderAPI.order(OrderCreatingData.INVALID_HREF, headers=headers)

        with allure.step('Проверка появление ошибки'):
            assert response.status_code == StatusCodes.INTERNAL_SERVER_ERROR

