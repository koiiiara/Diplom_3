from selenium.webdriver.common.by import By

class Locators:
    #Локатор для кнопки "Личный Кабинет"
    ACCOUNT_BUTTON = (By.XPATH, ".//header//*[text()='Личный Кабинет']")

    #Локатор для кнопки "Войти в аккаунт" на домашней странице
    ENTER_ACCOUNT_BUTTON = ".//button[text()='Войти в аккаунт']"

    #Кнопка ссылка "Войти"
    ENTER_ACCOUNT_LINK_BUTTON = (By.XPATH, ".//a[@href='/login' and text()='Войти']",)

    #Кнопка ссылка "Восстановить пароль" на странице входа
    RECOVER_PASS_BUTTON = (By.XPATH, ".//a[@href='/forgot-password' and text()='Восстановить пароль']",)

    #Локатор для кнопки "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    #Локатор для кнопки перехода на страницу регистрации
    GO_TO_REGISTER_BUTTON = (By.XPATH, ".//a[@href='/register' and text()='Зарегистрироваться']",)

    #Локатор для поля "Имя" в форме регистрации
    REGISTER_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/parent::div/input")

    #Локатор для поля "Email" в форме регистрации
    REGISTER_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::div/input")

    #Локатор для поля "Пароль" в форме регистрации
    REGISTER_PASS_FIELD = (By.XPATH, ".//input[@name='Пароль']")

    #Локатор для кнопки регистрации в форме регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    #Локатор для сообщения о некорректном пароле при регистрации
    INVALID_PASS_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

    #Локатор для поля "Email" в форме входа
    LOGIN_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::div/input")

    #Локатор для поля "Пароль" в форме входа
    LOGIN_PASS_FIELD = (By.XPATH, ".//input[@name='Пароль']")

    #Локатор для заголовка "Соберите бургер" на главной странице
    BUILD_BURGER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")

    #Локатор для кнопки "История заказов" на странице ЛК
    HISTORY_ORDERS_BUTTON = (By.XPATH, ".//a[@href='/account/order-history']")

    #Кнопка "Конструктор" в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//header//p[text()='Конструктор']")

    #Локатор для логотипа в хедере
    LOGO = (By.XPATH, ".//header//div[contains(@class, 'logo')]//a[@href='/']")

    #Локатор для кнопки "Выход" в ЛК
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    #Локатор для активной вкладки "Булки"
    ACTIVE_BUNS_BUTTON = (By.XPATH, ".//*[text()='Булки']/parent::div[contains(@class,'current')]")

    #Локатор для неактивной вкладки "Булки"
    INACTIVE_BUNS_BUTTON = (By.XPATH, ".//*[text()='Булки']/parent::div[not(contains(@class,'current')) and contains(@class, 'tab_tab')]")

    #Локатор для активной вкладки "Соусы"
    ACTIVE_SAUCE_BUTTON = (By.XPATH, ".//*[text()='Соусы']/parent::div[contains(@class,'current')]")

    #Локатор для неактивной вкладки "Соусы"
    INACTIVE_SAUCE_BUTTON = (By.XPATH, ".//*[text()='Соусы']/parent::div[not(contains(@class,'current')) and contains(@class, 'tab_tab')]")

    #Локатор для активной вкладки "Начинки"
    ACTIVE_TOPPING_BUTTON = (By.XPATH, ".//*[text()='Начинки']/parent::div[contains(@class,'current')]")

    #Локатор для неактивной вкладки "Начинки"
    INACTIVE_TOPPING_BUTTON = (By.XPATH, ".//*[text()='Начинки']/parent::div[not(contains(@class,'current')) and contains(@class, 'tab_tab')]")

    #Локатор для заголовка раздела "Булки" в конструкторе
    BUNS_LABEL = (By.XPATH, ".//*[contains(@class,'menuContainer')]//h2[text()='Булки']")

    # Локатор для заголовка раздела "Соусы" в конструкторе
    SAUCE_LABEL = (By.XPATH, ".//*[contains(@class,'menuContainer')]//h2[text()='Соусы']")

    # Локатор для заголовка раздела "Начинки" в конструкторе
    TOPPING_LABEL = (By.XPATH, ".//*[contains(@class,'menuContainer')]//h2[text()='Начинки']")