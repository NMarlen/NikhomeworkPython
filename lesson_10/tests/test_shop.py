import allure
from selenium.webdriver.remote.webdriver import WebDriver

from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage
from lesson_10.pages.cart_page import CartPage
from lesson_10.pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.story("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Покупка трёх товаров и проверка итоговой суммы")
@allure.description(
    "Авторизация на сайте, добавление трёх товаров в корзину, "
    "оформление заказа и проверка итоговой суммы.",
)
def test_shop_total(driver: WebDriver) -> None:
    """
    Сквозной сценарий покупки трёх товаров и проверки суммы заказа.

    Args:
        driver (WebDriver): Экземпляр WebDriver.

    Returns:
        None
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открываем страницу логина и авторизуемся"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем три товара в корзину"):
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")

    with allure.step("Переходим в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Проверяем, что в корзине три товара"):
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 3, "Ожидалось 3 товара в корзине"

    with allure.step("Переходим к оформлению заказа и заполняем форму"):
        cart_page.click_checkout()
        checkout_page.fill_form("Veronika", "Marlen", "12345")

    with allure.step("Проверяем итоговую сумму заказа"):
        total = checkout_page.get_total()
        assert total == 58.29, (
            f"Ожидали $58.29, получили ${total}"
        )
