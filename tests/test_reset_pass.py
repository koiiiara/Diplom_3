import allure

from data.urls import WebUrls
from pages.login_page import LoginPage
from pages.reset_pass_page import ResetPassPage
import data.global_vars as gv


@allure.suite("Сброс пароля пользователя")
class TestResetPassPage:

    @allure.title('Переход на страницу сброса пароля')
    @allure.description('Проверка перехода на страницу сброса пароля со страницы входа')
    def test_go_to_reset_page(self, open_login_page):
        page = LoginPage(open_login_page)
        page.click_to_reset_password()
        page = ResetPassPage(open_login_page)
        page.wait_page_load()
        assert page.get_page_url() == WebUrls.RESET_PASS_PAGE

    @allure.title('Заполнение "email" в клик по "Восстановить"')
    @allure.description(
        'Проверка заполнения поля "email" и успешный переход по страницу смены пароля при нажатии на "Восстановить"')
    def test_input_email_and_click_reset_button(self, driver, create_user):
        page = ResetPassPage(driver)
        page.open_reset_pass_page()
        page.fill_email_field(gv.USER_DATA["email"])
        page.click_reset_button()

        assert page.get_page_url() == WebUrls.RESET_CONFIRM_PAGE

    @allure.title('Проверка кнопки отображения пароля')
    @allure.description('Проверка отображения пароля при нажатии на иконку "глаз"')
    def test_click_show_password(self, driver, create_user):
        page = ResetPassPage(driver)
        page.open_reset_pass_page()
        page.fill_email_field(gv.USER_DATA["email"])
        page.click_reset_button()
        page.click_show_pass_button()
        assert page.is_password_field_focused()
