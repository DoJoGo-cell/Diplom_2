# Diplom_2 - Тестирование API сервиса Stellar Burger

Автоматизированные тесты для API сайта [Stellar Burger](https://stellarburgers.education-services.ru/).
Документация API [Ссылка](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/Api-Stellar_Burgers.pdf)
Проект проверяет следующие ручки API:
- Создание заказа
- Авторизация пользователя
- Регистрация пользователя

## Реализованные тесты (9 тестов):

### 1-4. Тесты создания заказа
- `test_order_creating_with_auth_ok` — проверка успешного создания заказа при авторизированном пользователе с ингредиентами
- `test_order_creating_without_auth_error` — проверка неудачного создания заказа при не авторизированном пользователе
- `test_order_creating_without_ingredients_bad_request` — проверка неудачного создания заказа без ингридиентов при авторизированном пользователе
- `test_order_creating_invalid_href_internal_server_error` — проверка неудачного заказа c неверным хэшем ингридиентов при авторизированном пользователе


### 5-6. Тесты авторизации пользователя
- `test_user_login_registered_user_ok` — проверка успешной авторизации существующего пользователя
- `test_user_login_invalid_data_unauthorized` — проверка появления ошибки при авторизация пользователя используя неверный логин и пароль

### 7-9. Тест регистрации пользователя
- `test_user_creating_generative_data_ok` — проверка успешного создания пользователя используя уникальные генеративные данные при заполненности всех обязательных полей
- `test_user_creating_duplicate_data_forbidden` — проверка появления ошибки при попытке создания уже зарегистрированного пользователя при заполненности всех обязательных полей
- `test_user_creating_empty_required_field_forbidden` — проверка появления ошибки при попытке создания пользователя при незаполненности обязательного поля

## Установить зависимости
pip install -r requirements.txt

## Запуск тестов
pytest -v tests/

## Просмотр Allure отчета
allure open allure_report

## Результат
1 failed, 8 passed in 26.76s