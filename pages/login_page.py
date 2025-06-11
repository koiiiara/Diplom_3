import allure

from data.urls import WebUrls
from locators.global_locators import GlobalLocators
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу входа")
    def open_login_page(self):
        self.go_to_url(WebUrls.LOGIN_PAGE)
        self.wait_page_load()

    @allure.step("Дожидаемся загрузки страницы входа")
    def wait_page_load(self):
        self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажимаем по кнопку 'Восстановить пароль'")
    def click_to_reset_password(self):
        self.click_to_element(LoginPageLocators.RECOVER_PASS_BUTTON)

    @allure.step("Заполняем реквизиты для входа")
    def fill_login_form(self, user_data):
        self.send_keys_to_element(LoginPageLocators.EMAIL_FIELD, user_data["email"])
        self.send_keys_to_element(LoginPageLocators.PASS_FIELD, user_data["password"])

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизуемся существующим пользователем")
    def login(self, user_data):
        self.fill_login_form(user_data)
        self.click_login_button()

    @allure.step("Нажимаем на кнопку 'Конструктор' в хедере")
    def click_to_constructor_button(self):
        self.click_to_element(GlobalLocators.CONSTRUCTOR_BUTTON)





