import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Добавить товары в корзину")
    def add_products(self, products_to_add: list = None) -> None:
        """
        Находит кнопки 'Add to cart' для списка названий и нажимает их.
        :param products_to_add: список строк с названиями товаров (list).
        :return: None
        """
        if products_to_add is None:
            products_to_add = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]

        for product_name in products_to_add:
            xpath = (
                f"//div[text()='{product_name}']/"
                "ancestor::div[@class='inventory_item']//button"
            )
            add_button = self._driver.find_element(By.XPATH, xpath)
            add_button.click()

    @allure.step("Нажать на иконку корзины")
    def go_to_cart(self) -> None:
        """Осуществляет переход в корзину. :return: None"""
        self._driver.get_result_link = self._driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        self._driver.get_result_link.click()
