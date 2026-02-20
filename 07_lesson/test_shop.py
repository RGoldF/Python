from shop_auth_page import AuthorizationPage
from shop_main_page import MainPage
from shop_cart_page import CartPage
from shop_order_page import Order


def test_shop(firefox_driver):
    auth_page = AuthorizationPage(firefox_driver)
    auth_page.open()
    auth_page.login_account('standard_user', 'secret_sauce')

    main_page = MainPage(firefox_driver)
    main_page.add_products()
    main_page.go_to_cart()

    cart_page = CartPage(firefox_driver)
    cart_page.click_checkout()

    order = Order(firefox_driver)
    order.fill_form('Holly', 'Molly', '12345')

    total = order.get_total_price()

    assert total == "Total: $58.29"
