from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Локатор для кнопки входа в аккаунт
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Локатор для кнопки "Восстановить пароль"
    RECOVER_PASS_BUTTON = (By.XPATH, ".//a[@href='/forgot-password' and text()='Восстановить пароль']",)

    # Локатор для поля "Email" в форме входа
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::div/input")

    # Локатор для поля "Пароль" в форме входа
    PASS_FIELD = (By.XPATH, ".//input[@name='Пароль']")
