from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/classattr")


time.sleep(1)


button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
button.click()


time.sleep(2)


driver.quit()
