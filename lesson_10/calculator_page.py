import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 50)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу с медленным калькулятором.
        :return: None
        """
        self.driver.get
        ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку в {delay_seconds} сек.")
    def set_delay(self, delay_seconds: int) -> 'CalculatorPage':
        """
        Устанавливает значение задержки выполнения операций.
        :param delay_seconds: время задержки в секундах (int).
        :return: экземпляр CalculatorPage (self).
        """
        delay_input = self.waiter.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> 'CalculatorPage':
        """
        Выполняет нажатие на кнопку калькулятора по её тексту.
        :param button_text: текст на кнопке (str).
        :return: экземпляр CalculatorPage (self).
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()
        return self

    @allure.step("Нажать 7")
    def press_7(self) -> 'CalculatorPage':
        """Нажимает цифру 7. :return: CalculatorPage"""
        return self.click_button("7")

    @allure.step("Нажать 8")
    def press_8(self) -> 'CalculatorPage':
        """Нажимает цифру 8. :return: CalculatorPage"""
        return self.click_button("8")

    @allure.step("Нажать плюс")
    def press_plus(self) -> 'CalculatorPage':
        """Нажимает символ '+'. :return: CalculatorPage"""
        return self.click_button("+")

    @allure.step("Нажать равно")
    def press_equals(self) -> 'CalculatorPage':
        """Нажимает символ '='. :return: CalculatorPage"""
        return self.click_button("=")

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result: str, timeout: int = 50) -> None:
        """
        Ожидает, пока в поле экрана появится искомый текст.
        :param expected_result: строка, которую ожидаем увидеть (str).
        :param timeout: максимальное время ожидания (int).
        :return: None
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"),
                                             str(expected_result))
        )

    @allure.step("Считать значение с экрана")
    def get_result(self) -> str:
        """
        Возвращает текущий текст, отображаемый на экране калькулятора.
        :return: текст результата (str).
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    @allure.step("Выполнить расчет 7 + 8")
    def calculate_7_plus_8(self, delay_seconds: int = 45) -> 'CalculatorPage':
        """
        Цепочка действий для сложения 7 и 8 с заданной задержкой.
        :param delay_seconds: задержка в секундах (int).
        :return: экземпляр CalculatorPage (self).
        """
        self.set_delay(delay_seconds)
        self.press_7()
        self.press_plus()
        self.press_8()
        self.press_equals()
        return self
