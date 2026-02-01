import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    option = Options()
    option.add_argument("--headless")
    browser = webdriver.Chrome(options=option)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
