import allure
import requests

from data_to_use import TestData
from methods import Methods


class TestCarrierLogin:
    @allure.title('Проверяем, что курьер может успешно авторизоваться')
    def test_carrier_login_success(self):
        methods = Methods()
        payload = methods.carrier_register()
        response = requests.post(TestData.CARRIER_LOGIN, data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверяем, что курьер не может успешно авторизоваться при не указании обязательного поля')
    def test_login_without_needed_field_fail(self):
        methods = Methods()
        payload = methods.carrier_register()
        del payload['login']
        response = requests.post(TestData.CARRIER_LOGIN, data=payload)
        assert response.status_code == 400 and response.json()['message'] == TestData.BAD_LOGIN

    @allure.title('Проверяем, что курьер не может успешно авторизоваться при указании неверных данных')
    def test_login_with_wrong_data_fail(self):
        methods = Methods()
        payload = methods.carrier_register()
        payload['password'] = '-'
        response = requests.post(TestData.CARRIER_LOGIN, data=payload)
        assert response.status_code == 404 and response.json()['message'] == TestData.NOT_FOUND

    @allure.title('Проверяем, что курьер не может успешно авторизоваться, если вводятся несуществующие данные')
    def test_login_not_existing_carrier_fail(self):
        methods = Methods()
        payload = methods.carrier_register()
        payload['password'] = 1
        response = requests.post(TestData.CARRIER_LOGIN, data=payload)
        assert response.status_code == 404 and response.json()['message'] == TestData.NOT_FOUND
