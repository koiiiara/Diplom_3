import allure

from data.urls import WebUrls
from locators.global_locators import GlobalLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.go_to_url(WebUrls.BASE_URL)
        self.wait_page_load()

    @allure.step("Дожидаемся загрузки главной страницы")
    def wait_page_load(self):
        self.find_element_with_wait(MainPageLocators.BUILD_BURGER_TITLE)

    @allure.step("Нажимаем по кнопку 'Личный кабинет'")
    def click_to_account_button(self):
        self.click_to_element(GlobalLocators.ACCOUNT_BUTTON)

    @allure.step("Нажимаем на кнопку 'Лента Заказов'")
    def click_to_order_list_button(self):
        self.click_to_element(GlobalLocators.ORDER_LIST_BUTTON)

    @allure.step("Нажимаем на ингредиент")
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.CRATER_BUN_ICON)

    @allure.step("Проверяем появление окна с информацией об ингредиенте")
    def is_ingredient_modal_displayed(self):
        return self.is_element_displayed(MainPageLocators.CRATER_BUN_MODAL)

    @allure.step("Нажимаем на кнопку закрытия всплывающего окна с информацией об ингредиенте")
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_ICON)

    @allure.step("Проверяем скрытие окна с информацией об ингредиенте")
    def is_ingredient_modal_hidden(self):
        return self.is_element_hidden(MainPageLocators.CRATER_BUN_MODAL)

    @allure.step("Добавляем в заказ булку")
    def add_ingredient_to_order(self):
        self.drug_and_drop(MainPageLocators.CRATER_BUN_ICON, MainPageLocators.BURGER_BASKET_AREA)

    @allure.step("Проверяем счетчик ингредиента")
    def get_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.BUN_COUNTER)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_to_order_create(self):
        self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Проверяем появление окна с информацией о заказе")
    def is_order_modal_displayed(self):
        self.find_element_with_wait(MainPageLocators.ORDER_MODAL_STATUS_TEXT)
        return self.is_element_displayed(MainPageLocators.ORDER_MODAL)

    @allure.step("Нажимаем на кнопку закрытия всплывающего окна с информацией об ингредиенте")
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_ICON)

    @allure.step("Проверяем скрытие окна с информацией о заказе")
    def is_order_modal_hidden(self):
        return self.is_element_hidden(MainPageLocators.ORDER_MODAL)

    @allure.step("Дожидаемся исчезновения анимации загрузки")
    def wait_load_animation_hide(self):
        self.wait_for_element_invisibility(GlobalLocators.LOAD_ANIMATION)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        self.wait_load_animation_hide()
        return int(self.get_text_from_element(MainPageLocators.ORDER_NUMBER))
