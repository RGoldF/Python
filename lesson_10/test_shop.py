import allure
from shop_auth_page import AuthorizationPage
from shop_main_page import MainPage
from shop_cart_page import CartPage
from shop_order_page import Order


@allure.title("Оформление покупки в онлайн-магазине")
@allure.description("Сценарий от авторизации до проверки итоговой суммы чека.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("smoke", "regression")
@allure.link("https://www.saucedemo.com/", name="Sauce Demo")
def test_shop(firefox_driver):
    """
    Тест проверяет сценарий покупки в интернет-магазине:
    1. Авторизация пользователя
    2. Добавление товаров в корзину
    3. Проверка содержимого корзины
    4. Оформление заказа
    5. Проверка итоговой суммы
    """
    with allure.step("Авторизация в системе"):
        auth_page = AuthorizationPage(firefox_driver)
        auth_page.open()
        auth_page.login_account('standard_user', 'secret_sauce')

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(firefox_driver)
        main_page.add_products()
        main_page.go_to_cart()

    with allure.step("Перейти к оформлению (Checkout)"):
        cart_page = CartPage(firefox_driver)
        cart_page.click_checkout()

    with allure.step("Заполнение формы персональными данными"):
        order = Order(firefox_driver)
        order.fill_form('Holly', 'Molly', '12345')

    with allure.step("Проверить, что финальная стоимость составляет $58.29"):
        total = order.get_total_price()
        assert total == "Total: $58.29"

        allure.attach(
            f"Фактическая сумма в чеке: {total}",
            name="Результат проверки",
            attachment_type=allure.attachment_type.TEXT
        )
