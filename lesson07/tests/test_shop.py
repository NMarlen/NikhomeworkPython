import pytest
from selenium import webdriver
from lesson07.pages.login_page import LoginPage
from lesson07.pages.inventory_page import InventoryPage
from lesson07.pages.cart_page import CartPage
from lesson07.pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Шаги по сценарию
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")

    inventory.go_to_cart()

    cart_items = cart.get_cart_items()
    assert len(cart_items) == 3, "Не все товары добавлены"

    cart.click_checkout()

    checkout.fill_form("Veronika", "Marlen", "12345")

    total = checkout.get_total()

    assert total == 58.29, f"Ожидали $58.29, получили ${total}"
