import pytest
from selenium import webdriver

from helpers.api_methods import UserMethods, OrderMethods
from helpers.user_generator import generate_user
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import data.global_vars as gv

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    gv.BROWSER = request.param

    if gv.BROWSER == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture()
def create_user():
    user_methods = UserMethods()
    user_data = generate_user()
    email = user_data["email"]
    password = user_data["password"]
    name = user_data["name"]
    status_code, response_json = user_methods.create_user(email, name, password)
    if status_code == 200:
        user_data["token"] = response_json["accessToken"]
        gv.USER_DATA = user_data
        yield user_data
    else:
        raise RuntimeError(
            f"Не удалось создать пользователя: {status_code}, {response_json}"
        )
    del_status_code, del_response = user_methods.delete_user(user_data["token"])
    if del_status_code != 202:
        raise RuntimeError(
            f"Не удалось удалить тестового пользователя после теста: {del_status_code}, {del_response}"
        )

@pytest.fixture()
def open_main_page_with_login(driver, create_user):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(gv.USER_DATA)
    main_page = MainPage(driver)
    main_page.wait_page_load()
    return driver

@pytest.fixture()
def open_account_page(open_main_page_with_login):
    driver = open_main_page_with_login
    main_page = MainPage(driver)
    main_page.click_to_account_button()
    return driver

@pytest.fixture()
def open_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    return driver

@pytest.fixture()
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    return driver

@pytest.fixture()
def open_feed_page(open_main_page):
    driver = open_main_page
    main_page = MainPage(driver)
    main_page.click_to_order_list_button()
    feed_page = FeedPage(driver)
    feed_page.wait_page_load()
    return driver

@pytest.fixture()
def create_orders(open_main_page_with_login):
    driver = open_main_page_with_login
    order_methods = OrderMethods()
    orders = []
    for i in range(2):
        ingredients = order_methods.get_random_ingredients_ids(3)
        status_code, response = order_methods.create_order(ingredients, gv.USER_DATA["token"])
        if status_code != 200:
            raise RuntimeError(
                f"Не удалось создать тестовый заказ: {status_code}, {response}"
            )
        order_num = f"{response.json()['order']['number']:07}"
        orders.append(order_num)
    return driver, orders




