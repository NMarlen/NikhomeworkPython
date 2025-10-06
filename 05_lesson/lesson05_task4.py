from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")


time.sleep(1)


username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")


username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")


login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()


time.sleep(2)


message = driver.find_element(By.ID, "flash").text


print("Сообщение от сайта:")
print(message)


driver.quit()
