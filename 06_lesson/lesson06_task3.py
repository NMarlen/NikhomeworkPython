from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 20)

wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "img")) >= 3)

images = driver.find_elements(By.CSS_SELECTOR, "img")

wait.until(lambda d: images[2].get_attribute("src") not in [None, ""])

third_image_src = images[2].get_attribute("src")

print(third_image_src)

driver.quit()
