import allure

from data.urls import WebUrls
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.suite("Личный кабинет")
class TestAccount:

    @allure.title('Переход в личный кабинет')
    @allure.description(
        'Проверка перехода на страницу профиля пользователя по клику на кнопку "Личный кабинет" на главной странице')
    def test_go_to_account_page(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_to_account_button()
        page = LoginPage(driver)
        page.wait_page_load()
        assert page.get_page_url() == WebUrls.LOGIN_PAGE

    @allure.title('Переход на страницу истории заказов')
    @allure.description(
        'Проверка перехода на страницу истории заказов по клику на кнопку "История заказов" на странице профиля')
    def test_go_to_order_history(self, open_account_page):
        page = AccountPage(open_account_page)
        page.wait_page_load()
        page.click_order_button()
        assert page.get_page_url() == WebUrls.ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    @allure.description('Проверка выхода из аккаунта пользователя по клику на кнопку "Выход" на странице профиля')
    def test_exit_from_account(self, open_account_page):
        page = AccountPage(open_account_page)
        page.wait_page_load()
        page.click_exit_button()
        page = LoginPage(open_account_page)
        page.wait_page_load()
        assert page.get_page_url() == WebUrls.LOGIN_PAGE
