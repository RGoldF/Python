import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthorizationPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Открыть страницу авторизации магазина")
    def open(self) -> None:
        """Открывает URL магазина. :return: None"""
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизоваться под пользователем {username}")
    def login_account(self, username: str, password: str) -> None:
        """
        Вводит данные пользователя и нажимает Login.
        :param username: имя пользователя (str).
        :param password: пароль (str).
        :return: None
        """
        self._driver.find_element(By.ID, "user-name").send_keys(username)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
