import allure

from data.urls import WebUrls
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.suite("Основной функционал")
class TestMainFunctions:

    @allure.title('Переход в конструктор')
    @allure.description(
        'Проверка перехода на страницу конструктора бергера по клику на кнопку "Конструктор"')
    def test_open_constructor(self, open_login_page):
        page = LoginPage(open_login_page)
        page.click_to_constructor_button()

        page = MainPage(open_login_page)
        page.wait_page_load()

        assert page.get_page_url() == WebUrls.BASE_URL

    @allure.title('Переход в ленту заказов')
    @allure.description(
        'Проверка перехода на страницу ленты заказов по клику на кнопку "Лента Заказов"')
    def test_open_order_list(self, open_main_page):
        page = MainPage(open_main_page)
        page.click_to_order_list_button()

        page = FeedPage(open_main_page)
        page.wait_page_load()

        assert page.get_page_url() == WebUrls.FEED_PAGE

    @allure.title('Открытие всплывающего окна ингредиента')
    @allure.description(
        'Проверка открытия всплывающего окна с деталями ингредиента по клику на ингредиент')
    def test_click_on_ingredient(self, open_main_page):
        page = MainPage(open_main_page)
        page.click_to_ingredient()

        assert (page.is_ingredient_modal_displayed() and
                page.get_page_url() == WebUrls.CRATER_BUN_MODAL)

    @allure.title('Закрытие всплывающего окна ингредиента')
    @allure.description(
        'Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик')
    def test_close_ingredient_modal(self, open_main_page):
        page = MainPage(open_main_page)
        page.click_to_ingredient()
        page.is_ingredient_modal_displayed()
        page.close_ingredient_modal()

        assert page.is_ingredient_modal_hidden()

    @allure.title('Изменение счетчика ингредиента')
    @allure.description(
        'Проверка изменения счетчика ингредиента при добавлении ингредиента в корзину')
    def test_ingredient_counter(self, open_main_page):
        page = MainPage(open_main_page)
        page.add_ingredient_to_order()
        assert int(page.get_ingredient_counter()) == 2

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description(
        'Проверка возможности создания заказа без авторизации')
    def test_create_order_no_auth(self, open_main_page_with_login):
        page = MainPage(open_main_page_with_login)
        page.add_ingredient_to_order()
        page.click_to_order_create()
        assert page.is_order_modal_displayed()








