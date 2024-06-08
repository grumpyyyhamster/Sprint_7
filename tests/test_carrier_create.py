import allure
import requests

from data_to_use import TestData
from methods import Methods

class TestCarrierCreate:

    @allure.title('Проверяем успешное создание курьера')
    def test_carrier_create_success(self):
        methods = Methods()
        payload = methods.generate_random_reg_data()
        response = requests.post(TestData.CARRIER_CREATE, data=payload)
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_carrier_duplicate_create_fail(self):
        methods = Methods()
        payload = methods.generate_random_reg_data()
        requests.post(TestData.CARRIER_CREATE, data=payload)
        response = requests.post(TestData.CARRIER_CREATE, data=payload)
        assert response.status_code == 409 and response.json()['message'] == TestData.SAME_LOGIN

    @allure.title('Проверяем, что нельзя создать курьера без указания обязательного поля')
    def test_carrier_create_without_needed_field_fail(self):
        methods = Methods()
        payload = methods.generate_random_reg_data()
        del payload['login']
        response = requests.post(TestData.CARRIER_CREATE, data=payload)
        assert response.status_code == 400 and response.json()['message'] == TestData.BAD_CREATION