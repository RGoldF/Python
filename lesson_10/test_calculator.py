import allure
from calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Сложение 7 и 8 с ожиданием результата в течение 50 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.calculate_7_plus_8(delay_seconds=45)
    calc_page.wait_for_result("15", timeout=50)

    with allure.step("Проверить, что итоговый результат на экране равен 15"):
        assert calc_page.get_result() == "15"
