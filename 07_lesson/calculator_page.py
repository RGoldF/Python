from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_seconds):
        delay_input = self.waiter.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self

    def click_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()
        return self

    def press_7(self): return self.click_button("7")
    def press_8(self): return self.click_button("8")
    def press_plus(self): return self.click_button("+")
    def press_equals(self): return self.click_button("=")

    def wait_for_result(self, expected_result, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), str(expected_result))
        )

    def get_result(self):
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def calculate_7_plus_8(self, delay_seconds=45):
        self.set_delay(delay_seconds)
        self.press_7()
        self.press_plus()
        self.press_8()
        self.press_equals()
        return self
