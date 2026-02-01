from selenium.webdriver.common.by import By

class Homepage:

    def __init__(self, browser):
        self.browser = browser

    def open_homepage(self):
        self.browser.get("https://www.demoblaze.com/")

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitors(self):
        monitors = self.browser.find_element(By.XPATH, '//a[text()="Monitors"]')
        monitors.click()

    def check_product_count(self, count):
        products = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(products) == count