from selenium.webdriver.common.by import By
from time import sleep


def test_add_to_basket_button(browser):
    button = browser.find_element(
        By.CSS_SELECTOR,
        "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    sleep(30)
    assert button, 'No button here'
