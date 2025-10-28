from lesson07.pages.calculator_page import CalculatorPage



def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.open()

    page.set_delay(2)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result()
    assert result == "15", f"Ожидали 15, получили {result}"
