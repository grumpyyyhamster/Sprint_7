import json

import allure
import pytest
import requests

from data_to_use import TestData


class TestCreateOrder:

    @allure.title('Проверяем, что возможно успешно создать заказ с различными цветами самоката')
    @pytest.mark.parametrize('reg_data', [TestData.REG_DATA_USER_1, TestData.REG_DATA_USER_2, TestData.REG_DATA_USER_3])
    def test_make_order(self, reg_data):
        payload = json.dumps(reg_data)
        response = requests.post(TestData.ORDER, payload)
        assert response.status_code == 201 and 'track' in response.json()