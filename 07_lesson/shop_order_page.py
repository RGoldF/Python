from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Order:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        total_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
