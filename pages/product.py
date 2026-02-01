from selenium.webdriver.common.by import By

class Product_page:
    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, "h2")
        page_title_text = title
        