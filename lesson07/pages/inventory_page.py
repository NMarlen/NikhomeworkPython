from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{formatted_name}")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
