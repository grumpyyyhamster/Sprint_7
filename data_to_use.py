class TestData:
    #регистрационный набор данных юзера 1
    REG_DATA_USER_1 = {
        "firstName": "Джессика",
        "lastName": "Вайт",
        "address": "улица Мира, дом 18",
        "metroStation": 2,
        "phone": "+7 111 111 11 11",
        "rentTime": 2,
        "deliveryDate": "2024-06-20",
        "comment": "Позвоните за час до доставки, пожалуйста",
        "color": ["BLACK"]
    }
    #регистрационный набор данных юзера 2
    REG_DATA_USER_2 = {
        "firstName": "Энтони",
        "lastName": "Блу",
        "address": "бульвар Ломоносова, дом 18",
        "metroStation": 7,
        "phone": "+7 111 111 11 11",
        "rentTime": 7,
        "deliveryDate": "2024-07-18",
        "comment": "Около нашего дома стоит забор с домофоном, код 123",
        "color": ["BLACK","GREY"]
    }
    #регистрационный набор данных юзера 3
    REG_DATA_USER_3 = {
        "firstName": "Кэтти",
        "lastName": "Грин",
        "address": "улица Ошарская, дом 33",
        "metroStation": 4,
        "phone": "+7 111 111 11 11",
        "rentTime": 4,
        "deliveryDate": "2024-08-19",
        "comment": "Рядом с домом ведутся ремонтные работы, будьте осторожны",
        "color": [""]
    }

    #список ответов для логина курьера
    BAD_LOGIN = 'Недостаточно данных для входа'
    NOT_FOUND = 'Учетная запись не найдена'

    #список ответов для создания курьера
    BAD_CREATION = 'Недостаточно данных для создания учетной записи'
    SAME_LOGIN = 'Этот логин уже используется. Попробуйте другой.'

    #список необходимых эндпоинтов
    CARRIER_CREATE = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    CARRIER_LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    ORDER = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
