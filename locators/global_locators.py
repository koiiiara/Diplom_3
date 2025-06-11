from selenium.webdriver.common.by import By


class GlobalLocators:
    # Локатор любого всплывающего окна
    MODAL_WINDOW = (By.XPATH, ".//div[contains(@class, 'Modal_modal__P3_V5')]")#/child::*")

    # Локатор для кнопки "Конструктор" в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//header//p[text()='Конструктор']")

    # Локатор для кнопки "Лента заказов" в хедере
    ORDER_LIST_BUTTON = (By.XPATH, ".//header//p[text()='Лента Заказов']")

    # Локатор для анимации загрузки
    LOAD_ANIMATION = (By.XPATH, ".//div[contains(@class, 'Modal_modal__P3_V5')]")

    # Локатор для кнопки "Личный Кабинет" в хедере
    ACCOUNT_BUTTON = (By.XPATH, ".//header//*[text()='Личный Кабинет']")
