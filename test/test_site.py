import time
from pages.homepage import Homepage
from pages.product import Product_page

def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open_homepage()
    homepage.click_galaxy_s6()
    product_page = Product_page(browser)
    product_page.check_title_is("Samsung galaxy s6")

def test_number_of_monitors(browser):
    homepage = Homepage(browser)
    homepage.open_homepage()
    homepage.click_monitors()
    time.sleep(2)
    homepage.check_product_count(2)

  