import allure

from data.urls import WebUrls
from pages.base_page import BasePage
from locators.reset_pass_page_locators import ResetPassPageLocators


class ResetPassPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу восстановления пароля")
    def open_reset_pass_page(self):
        self.go_to_url(WebUrls.RESET_PASS_PAGE)
        self.wait_page_load()

    @allure.step("Дожидаемся загрузки страницы восстановления пароля")
    def wait_page_load(self):
        self.find_element_with_wait(ResetPassPageLocators.RESET_PASS_TITLE)

    @allure.step("Заполняем поле email")
    def fill_email_field(self, email):
        self.send_keys_to_element(ResetPassPageLocators.RESET_PASS_EMAIL_FIELD, email)

    @allure.step("Заполняем по ле 'Пароль'")
    def fill_password_field(self, password):
        self.send_keys_to_element(ResetPassPageLocators.NEW_PASSWORD_FIELD, password)

    @allure.step("Нажимаем кнопку 'Восстановить' и ждем перехода")
    def click_reset_button(self):
        self.click_to_element(ResetPassPageLocators.RESET_BUTTON)
        self.find_element_with_wait(ResetPassPageLocators.CODE_FROM_MAIL_FIELD)

    @allure.step("Нажимаем на кнопку скрыть/показать пароль")
    def click_show_pass_button(self):
        self.click_to_element(ResetPassPageLocators.SHOW_PASS_BUTTON)

    @allure.step("Проверяем, что поле 'пароль' активно")
    def is_password_field_focused(self):
        is_active = self.is_element_contains_value_in_attribute(ResetPassPageLocators.NEW_PASSWORD_FIELD,
                                                                "class",
                                                                "input__placeholder-focused")
        return is_active
