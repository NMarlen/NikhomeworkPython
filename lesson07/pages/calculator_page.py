from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value: int):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, label: str):
        locator = (By.XPATH, f"//span[text()='{label}']")
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", button)

    def get_result(self):
        screen = (By.CLASS_NAME, "screen")
        WebDriverWait(self.driver, 60).until(
            lambda d: d.find_element(*screen).text not in ["", "Calculating", "7+8"]
        )
        return self.driver.find_element(*screen).text
