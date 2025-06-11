from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Локатор для заголовка "Лента заказов" на главной странице ленты заказов
    ORDER_LIST_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")

    # Локатор для всплывающего окна деталей заказа
    ORDER_DETAIL_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]")

    # Локатор для любого номера заказа в списке заказов
    ORDER_NUMBER = (
        By.XPATH,
        ".//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')]")

    # Форматируемый локатор номера заказа в ленте заказов
    FORMAT_ORDER_NUMBER = (
        By.XPATH,
        ".//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')][text()='#{}']")

    # Локатор для счетчика заказов за день
    DAILY_ORDERS_COUNTER = (
        By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::div/p[contains(@class, 'ext_type_digits-large')]")

    # Локатор для счетчика заказов за все время
    ALL_ORDERS_COUNTER = (
        By.XPATH, ".//p[text()='Выполнено за все время:']/parent::div/p[contains(@class, 'ext_type_digits-large')]")

    # Форматируемый локатор для заказа в работе
    ORDER_NUM_IN_WORK = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[text()={}]")
