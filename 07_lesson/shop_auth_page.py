from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthorizationPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get("https://www.saucedemo.com/")

    def login_account(self, username, password):
        self._driver.find_element(By.ID, "user-name").send_keys(username)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
