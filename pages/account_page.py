import allure

from data.urls import WebUrls
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Открываем страницу профиля пользователя")
    def open_account_page(self):
        self.go_to_url(WebUrls.USER_PROFILE)
        self.wait_page_load()

    @allure.step("Дожидаемся загрузки страницы профиля пользователя")
    def wait_page_load(self):
        self.find_element_with_wait(AccountPageLocators.HISTORY_ORDERS_BUTTON)

    @allure.step("Нажимаем на кнопку 'История заказов'")
    def click_order_button(self):
        self.click_to_element(AccountPageLocators.HISTORY_ORDERS_BUTTON)

    @allure.step("Нажимаем на кнопку выхода из аккаунта")
    def click_exit_button(self):
        self.click_to_element(AccountPageLocators.EXIT_BUTTON)
