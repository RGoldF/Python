import allure
from calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест проверяет сложение 7 + 8 и ожидание результата "
    "при задержке 45 сек."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("smoke", "math")
def test_slow_calculator(browser):
    """
    Тест проверяет работу калькулятора с задержкой:
    1. Отк
    2. Сложение 7 + 8
    3. Ожидание результата 15
    4. Проверка полученного результата
    """
    with allure.step("Инициализация страницы калькулятора"):
        calculator_page = CalculatorPage(browser)
        allure.attach(
            "URL: "
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html",
            name="Страница",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Открыть главную страницу калькулятора"):
        calculator_page.open()

    with allure.step("Ввести пример: 7 + 8 с задержкой 45 секунд"):
        calculator_page.calculate_7_plus_8(delay_seconds=45)

    with allure.step("Дождаться появления результата '15'"):
        calculator_page.wait_for_result("15", timeout=50)

    with allure.step("Проверить, что итоговое значение на экране равно 15"):
        final_result = calculator_page.get_result()
        assert final_result == "15"
    with allure.step("Тест успешно завершен"):
        allure.attach(
            "Калькулятор работает корректно с задержкой 45 секунд",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )
