from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Страница авторизации интернет-магазина SauceDemo.
    """

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует объект страницы логина.

        Args:
            driver (WebDriver): Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу логина.

        Returns:
            None
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию с указанным логином и паролем.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
