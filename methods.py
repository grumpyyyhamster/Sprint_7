import allure
import requests
import random
import string

from data_to_use import TestData


class Methods:
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Генирируем данные для того, чтобы зарегистрировать курьера')
    def generate_random_reg_data(self):
        reg_login = self.generate_random_string(5)
        reg_password = self.generate_random_string(5)
        reg_name = self.generate_random_string(5)

        payload = {
            "login": reg_login,
            "password": reg_password,
            "firstName": reg_name
        }
        return payload


    @allure.step('Регистрируем пользователя')
    def carrier_register(self):
        payload = self.generate_random_reg_data()
        requests.post(TestData.CARRIER_CREATE, data=payload)
        return payload
