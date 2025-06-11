import random
import string

import allure

@allure.step("Генерируем уникального пользователя")
def generate_user():
    # генерируем email, пароль и имя пользователя
    email = generate_random_string(10) + "@" + "yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    # возвращаем список
    return {
        "email": email,
        "password": password,
        "name": name
    }


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
@allure.step("Генерируем случайную строку")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
