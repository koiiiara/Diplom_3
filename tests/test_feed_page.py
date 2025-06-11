import allure

from conftest import create_orders
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.suite("Лента заказов")
class TestFeedPage:

    @allure.title('Открытие всплывающего окна с информацией о заказе')
    @allure.description(
        'Проверка открытия всплывающего окна с детальной информацией о заказе по клику на заказ')
    def test_click_on_order(self, open_feed_page):
        page = FeedPage(open_feed_page)
        page.click_to_order()
        assert page.is_order_modal_displayed()

    @allure.title('Отображение заказов пользователя в ленте заказов')
    @allure.description(
        'Проверка появления заказов пользователя в ленте заказов')
    def test_show_user_orders_in_order_list(self, create_orders):
        web_driver, orders = create_orders
        page = MainPage(web_driver)
        page.click_to_order_list_button()
        page = FeedPage(web_driver)
        page.wait_orders_exist_in_order_list(orders)
        orders_list = page.get_orders_numbers()
        assert page.check_user_orders_in_orders_list(orders, orders_list)

    @allure.title("Увеличение счетчика дневных заказов за день")
    @allure.description("Проверка увеличения счетчика заказов за день после создания нового заказа")
    def test_daily_orders_counter_increase(self, open_main_page_with_login):
        main_page = MainPage(open_main_page_with_login)
        feed_page = FeedPage(open_main_page_with_login)
        feed_page.open_feed_page()
        init_orders_count = feed_page.get_daily_orders_count()
        main_page.open_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_to_order_create()
        main_page.is_order_modal_displayed()
        main_page.wait_load_animation_hide()
        feed_page.open_feed_page()
        feed_page.wait_daily_orders_increase(init_orders_count)
        assert init_orders_count < feed_page.get_daily_orders_count()

    @allure.title("Увеличение счетчика дневных заказов за все время")
    @allure.description("Проверка увеличения счетчика заказов за все время после создания нового заказа")
    def test_all_orders_counter_increase(self, open_main_page_with_login):
        main_page = MainPage(open_main_page_with_login)
        feed_page = FeedPage(open_main_page_with_login)
        feed_page.open_feed_page()
        init_orders_count = feed_page.get_all_orders_count()
        main_page.open_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_to_order_create()
        main_page.is_order_modal_displayed()
        main_page.wait_load_animation_hide()
        feed_page.open_feed_page()
        feed_page.wait_all_orders_increase(init_orders_count)
        assert init_orders_count < feed_page.get_all_orders_count()


    @allure.title('Отображение номера заказа в разделе "В работе"')
    @allure.description(
        'Проверка появления номера заказа в в разделе "В работе" в ленте заказов')
    def test_order_in_work(self, open_main_page_with_login):
        main_page = MainPage(open_main_page_with_login)
        feed_page = FeedPage(open_main_page_with_login)
        main_page.open_main_page()
        main_page.add_ingredient_to_order()
        main_page.click_to_order_create()
        main_page.is_order_modal_displayed()
        order_number = main_page.get_order_number()
        feed_page.open_feed_page()
        order_element = feed_page.wait_order_to_be_in_work(order_number)
        assert order_element.text == f"0{order_number}"
