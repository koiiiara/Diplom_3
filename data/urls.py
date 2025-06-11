class WebUrls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = BASE_URL + "login"
    RESET_PASS_PAGE = BASE_URL + "forgot-password"
    RESET_CONFIRM_PAGE = BASE_URL + "reset-password"
    ORDER_HISTORY = BASE_URL + "account/order-history"
    USER_PROFILE = BASE_URL + "account/profile"
    FEED_PAGE = BASE_URL + "feed"
    CRATER_BUN_MODAL = BASE_URL + "ingredient/61c0c5a71d1f82001bdaaa6c"


class ApiUrls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    USER_URL = BASE_URL + "/auth/user"
    USER_REGISTER_URL = BASE_URL + "/auth/register"
    ORDER_URL = BASE_URL + "/orders"
    INGREDIENTS_URL = BASE_URL + "/ingredients"
