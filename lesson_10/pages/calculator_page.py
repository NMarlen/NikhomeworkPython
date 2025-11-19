from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Страница медленного калькулятора.
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует объект страницы калькулятора.

        Args:
            driver (WebDriver): Экземпляр WebDriver.
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get(self.URL)

    def set_delay(self, value: int) -> None:
        """
        Устанавливает задержку вычисления результата.

        Args:
            value (int): Задержка в секундах.

        Returns:
            None
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, label: str) -> None:
        """
        Нажимает кнопку калькулятора по её подписи.

        Args:
            label (str): Текст на кнопке (цифра или знак операции).

        Returns:
            None
        """
        locator = (By.XPATH, f"//span[text()='{label}']")
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_result(self) -> str:
        """
        Ожидает появления результата на экране и возвращает его.

        Returns:
            str: Строковое значение результата вычисления.
        """
        screen = (By.CLASS_NAME, "screen")
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element(*screen).text not in (
                "",
                "Calculating",
                "7+8",
            ),
        )
        return self.driver.find_element(*screen).text
