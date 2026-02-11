from calculator_page import CalculatorPage


def test_slow_calculator(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()

    calc_page.calculate_7_plus_8(delay_seconds=45)

    calc_page.wait_for_result("15", timeout=50)

    assert calc_page.get_result() == "15"
