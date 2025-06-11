from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локатор заголовка на главной странице
    BUILD_BURGER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")

    # Локатор кнопки создания заказа
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'button_button_type_primary__1O7Bx')]")

    # Локатор булки "Краторная булка N-200i"
    CRATER_BUN_ICON = (By.XPATH, ".//p[text()='Краторная булка N-200i']")

    # Локатор всплывающего окна с информацией о булке:"Краторная булка N-200i"
    CRATER_BUN_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal__P3_V5')]")

    # Локатор кнопки закрытия всплывающего окна с информацией о булке
    CLOSE_MODAL_ICON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close__TnseK')]")

    # Локатор корзины для перетаскивания ингредиентов
    BURGER_BASKET_AREA = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket__list__l9dp_')]")

    # Локатор счетчика ингредиента
    BUN_COUNTER = (
        By.XPATH,
        ".//p[text()='Краторная булка N-200i']/parent::a/div/p[contains(@class, 'counter_counter__num__3nue1')]")

    # Локатор всплывающего окна при успешном заказе
    ORDER_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]")

    # Локатор текста во всплывающем окне при успешном заказе
    ORDER_MODAL_STATUS_TEXT = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")

    # Локатор номера заказа во всплывающем окне при успешном заказе
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title__2L34m')]")
