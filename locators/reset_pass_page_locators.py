from selenium.webdriver.common.by import By


class ResetPassPageLocators:
    # Локатор заголовка страницы сброса пароля
    RESET_PASS_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']",)

    # Локатор поля email
    RESET_PASS_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::div/input")

    # Локатор кнопки восстановить
    RESET_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    # Локатор поля ввода нового пароля
    NEW_PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']")

    # Локатор поля ввода кода подтверждения из письма
    CODE_FROM_MAIL_FIELD = (By.XPATH, ".//label[text()='Введите код из письма']/parent::div/input")

    # Локатор иконки показать/скрыть пароль
    SHOW_PASS_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon-action')]/child::*")
