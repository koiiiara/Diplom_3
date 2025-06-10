from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import data.global_vars as gv
from locators.global_locators import GlobalLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def get_page_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*locator))

    def click_to_element(self, locator):
        if gv.BROWSER == "firefox":
            self.wait_for_element_invisibility(GlobalLocators.MODAL_WINDOW)

        self.find_element_with_wait(locator).click()

    def send_keys_to_element(self, locator, keys):
        self.find_element_with_wait(locator).send_keys(keys)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def send_return_to_element(self, locator):
        self.find_element_with_wait(locator).send_keys(Keys.RETURN)

    def is_element_contains_value_in_attribute(self, locator, attribute, value):
        element = self.find_element_with_wait(locator)
        if value in element.get_attribute(attribute).split(" "):
            return True
        return False

    def wait_for_element_invisibility(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
        return element

    def switch_window_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_element_displayed(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def is_element_hidden(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def drug_and_drop(self, locator_from, locator_to):
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        if gv.BROWSER == "firefox":
            self.driver.execute_script("""
                            const [from_element, to_element] = arguments;
                            const dataTransfer = new DataTransfer();

                            // Эмуляция событий drag-and-drop
                            ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                                const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                                (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
                            });
                        """, element_from, element_to)
        else:
            ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    def format_locator(self, locator, text):
        by, locator_str = locator
        locator_str = locator_str.format(text)
        return by, locator_str

    def wait_condition(self, condition):
         return WebDriverWait(self.driver, 10).until(condition)
