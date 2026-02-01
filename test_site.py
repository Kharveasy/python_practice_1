import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser


def test_open_s6(browser):
    browser.get("https://www.demoblaze.com/")
    galaxy_s6 = browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, "h2")
    assert title.text == "Samsung galaxy s6"

def test_number_of_monitors(browser):
    browser.get("https://www.demoblaze.com/")
    monitors = browser.find_element(By.XPATH, '//a[text()="Monitors"]')
    monitors.click()
    time.sleep(2)
    number_of_monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(number_of_monitors) == 2
