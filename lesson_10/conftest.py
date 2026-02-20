import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.implicitly_wait(10)
        driver.maximize_window()

    yield driver

    with allure.step("Закрытие браузера Chrome"):
        driver.quit()


@pytest.fixture
def firefox_driver():
    with allure.step("Запуск браузера Firefox"):
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.implicitly_wait(5)
        driver.maximize_window()

    yield driver

    with allure.step("Закрытие браузера Firefox"):
        driver.quit()
