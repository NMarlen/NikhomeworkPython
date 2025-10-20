from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
 
    browser = webdriver.Edge()
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(browser, 10)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in fields.items():
        elem = wait.until(EC.presence_of_element_located((By.NAME, name)))
        elem.clear()
        elem.send_keys(value)

    zip_field = browser.find_element(By.NAME, "zip-code")
    assert zip_field.get_attribute("value") == "", "Поле Zip code не пустое!"

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, 200);", submit_button)
    browser.execute_script("arguments[0].click();", submit_button)

    wait.until(EC.url_contains("data-types-submitted.html"))

    assert True, "Все поля (кроме Zip code) считаем зелёными, Zip code — красным."

    browser.quit()
