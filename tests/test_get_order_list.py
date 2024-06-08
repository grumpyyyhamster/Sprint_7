import allure
import requests

from data_to_use import TestData


class TestGetOrderList:

    @allure.title('Проверяем, что в тело ответа успешно возвращается список заказов')
    def test_get_order_list(self):
        response = requests.get(TestData.ORDER)
        assert response.status_code == 200 and 'orders' in response.json()
