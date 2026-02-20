import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Получить список товаров в корзине")
    def get_cart_items(self) -> list:
        """
        Считывает названия всех добавленных товаров в корзине.
        :return: список названий товаров (list[str]).
        """
        wait = WebDriverWait(self._driver, 10)
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )
        items = self._driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
        return [item.text for item in items]

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Переходит к оформлению заказа. :return: None"""
        self._driver.find_element(By.ID, "checkout").click()
