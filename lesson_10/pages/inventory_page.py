from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """
    Страница со списком товаров (inventory).
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует объект страницы списка товаров.

        Args:
            driver (WebDriver): Экземпляр WebDriver.
        """
        self.driver = driver

    def add_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар в корзину по его отображаемому имени.

        Args:
            item_name (str): Название товара, как на странице.

        Returns:
            None
        """
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{formatted_name}")
        self.driver.find_element(*locator).click()

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        Returns:
            None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
