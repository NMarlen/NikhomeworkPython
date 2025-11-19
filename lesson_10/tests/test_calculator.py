import allure
from selenium.webdriver.remote.webdriver import WebDriver

from lesson_10.pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Медленный калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка сложения 7 + 8")
@allure.description(
    "Открытие страницы медленного калькулятора, "
    "установка задержки и проверка корректности результата 7 + 8.",
)
def test_calculator_addition(driver: WebDriver) -> None:
    """
    Проверяет корректность сложения 7 + 8 на медленном калькуляторе.

    Args:
        driver (WebDriver): Экземпляр WebDriver.

    Returns:
        None
    """
    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку вычисления"):
        page.set_delay(2)

    with allure.step("Выполняем выражение 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Ожидаем и считываем результат"):
        result = page.get_result()

    with allure.step("Проверяем, что результат равен 15"):
        assert result == "15", f"Ожидали 15, получили {result}"
