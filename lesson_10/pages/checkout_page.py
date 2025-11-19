from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Страница оформления заказа (checkout).
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует объект страницы оформления заказа.

        Args:
            driver (WebDriver): Экземпляр WebDriver.
        """
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """
        Заполняет форму данными покупателя и переходит к следующему шагу.

        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> float:
        """
        Возвращает итоговую сумму заказа.

        Returns:
            float: Итоговая сумма в долларах.
        """
        total_text = self.driver.find_element(
            By.CLASS_NAME,
            "summary_total_label",
        ).text
        return float(total_text.replace("Total: $", ""))
