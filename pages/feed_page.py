import allure

from data.urls import WebUrls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step("Открываем страницу ленты заказов")
    def open_feed_page(self):
        self.go_to_url(WebUrls.FEED_PAGE)

    @allure.step("Дожидаемся загрузки страницы ленты заказов")
    def wait_page_load(self):
        self.find_element_with_wait(FeedPageLocators.ORDER_LIST_TITLE)

    @allure.step("Нажимаем на заказ в листе заказов")
    def click_to_order(self):
        self.click_to_element(FeedPageLocators.ORDER_NUMBER)

    @allure.step("Проверяем появление окна с информацией о заказе")
    def is_order_modal_displayed(self):
        return self.is_element_displayed(FeedPageLocators.ORDER_DETAIL_MODAL)

    @allure.step("Получаем список последних заказов")
    def get_orders_numbers(self):
        orders_nums = []
        orders_elements = self.find_elements_with_wait(FeedPageLocators.ORDER_NUMBER)
        for element in orders_elements:
            order_num = element.text.replace("#", "")
            orders_nums.append(order_num)
        return orders_nums

    @allure.step("Проверяем наличие заказов пользователя в списке всех заказов")
    def check_user_orders_in_orders_list(self, user_orders, orders_list):
        return set(user_orders).issubset(set(orders_list))

    @allure.step("Получаем количество заказов за день")
    def get_daily_orders_count(self):
        return int(self.get_text_from_element(FeedPageLocators.DAILY_ORDERS_COUNTER))

    @allure.step("Получаем количество заказов за все время")
    def get_all_orders_count(self):
        return int(self.get_text_from_element(FeedPageLocators.ALL_ORDERS_COUNTER))

    @allure.step("Дожидаемся, когда заказ поступит в работу")
    def wait_order_to_be_in_work(self, order_num):
        formated_num = f"{order_num}"
        locator = self.format_locator(FeedPageLocators.ORDER_NUM_IN_WORK, str(formated_num))
        return self.find_element_with_wait(locator)

    @allure.step("Ждем пока кол-во заказов за день увеличится")
    def wait_daily_orders_increase(self, old_count):
        self.wait_condition(lambda _: self.order_count_increased_condition(
            FeedPageLocators.DAILY_ORDERS_COUNTER, int(old_count)
        ))
    @allure.step("Ждем пока кол-во заказов за все время увеличится")
    def wait_all_orders_increase(self, old_count):
        self.wait_condition(lambda _: self.order_count_increased_condition(
            FeedPageLocators.ALL_ORDERS_COUNTER, int(old_count)
        ))

    @allure.step("Ждем появление заказов в ленте")
    def wait_orders_exist_in_order_list(self, orders):
        for order in orders:
            formated_locator = self.format_locator(FeedPageLocators.FORMAT_ORDER_NUMBER, str(order))
            self.find_element_with_wait(formated_locator)

    def order_count_increased_condition(self, locator, old_value):
        current_value = int(self.get_text_from_element(locator))
        if current_value > old_value:
            return True
        return False
