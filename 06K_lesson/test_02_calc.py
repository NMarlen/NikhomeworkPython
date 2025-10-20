import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # инициализация ChromeDriver (убедитесь, что chromedriver доступен)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    wait = WebDriverWait(browser, 60)  # даём чуть больше времени

    # 1. Вводим задержку 45 секунд
    delay_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # 2. Нажимаем кнопки: 7 + 8 =
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    # 3. Ждём, пока на экране появится результат “15”
    result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # 4. Получаем текст и проверяем
    screen = browser.find_element(By.CSS_SELECTOR, ".screen")
    result_text = screen.text.strip()
    assert result_text == "15", f"Ожидали результат 15, но получили {result_text}"
