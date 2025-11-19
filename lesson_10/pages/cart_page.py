from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    """
    Страница корзины.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует объект страницы корзины.

        Args:
            driver (WebDriver): Экземпляр WebDriver.
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "checkout").click()

    def get_cart_items(self) -> List[str]:
        """
        Возвращает список названий товаров в корзине.

        Returns:
            list[str]: Список строк с названиями товаров.
        """
        items: list[WebElement] = self.driver.find_elements(
            By.CLASS_NAME,
            "inventory_item_name",
        )
        return [item.text for item in items]
