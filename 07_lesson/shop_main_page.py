from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_products(self, products_to_add=None):
        if products_to_add is None:
            products_to_add = ["Sauce Labs Backpack",
                               "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]

        for product_name in products_to_add:
            xpath = (
                f"//div[text()='{product_name}']/ancestor::"
                f"div[@class='inventory_item']//button"
            )
            add_button = self._driver.find_element(By.XPATH, xpath)
            add_button.click()

    def go_to_cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
