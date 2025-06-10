from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Локатор для кнопки "Профиль" на странице ЛК
    PROFILE_BUTTON = (By.XPATH, ".//a[@href='/account/profile']")

    # Локатор для кнопки "История заказов" на странице ЛК
    HISTORY_ORDERS_BUTTON = (By.XPATH, ".//a[@href='/account/order-history']")

    # Локатор для кнопки "Выход" на странице ЛК
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
