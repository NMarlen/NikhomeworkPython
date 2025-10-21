import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_total():

    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for item_id in items_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    driver.find_element(By.ID, "first-name").send_keys("Veronika")
    driver.find_element(By.ID, "last-name").send_keys("Marlen")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    print(f"\nИтог с сайта: {total_text}")

    assert total_text == "Total: $58.29", f"❌ Ошибка: ожидалось 'Total: $58.29', а получено {total_text}"

    time.sleep(2)
    driver.quit()
