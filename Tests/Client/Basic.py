import re
from playwright.async_api import Playwright
from Common import LoginCredsReader
from Models.CheckoutPage import CheckoutPage
from Models.ShoppingPage import ShoppingPage

login_creds_reader = LoginCredsReader
webpageURL = login_creds_reader.webUrl


# expectedTitle = propsReader.main_Page_Title

class Basic:
    """
    Basic class - represents the base for all tests - all tests should inherit this object
    """
    global shoppingPage

    def __init__(self, playwright: Playwright):
        self.webpageURL = webpageURL
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def login(self):
        global shoppingPage
        shoppingPage = ShoppingPage(self.page, webpageURL)
        shoppingPage.login()

    def go_shopping(self):
        shoppingPage.dropit_burger_purchase_scenario()

    def go_shopping_neg(self):
        shoppingPage.dropit_neg_scenario()

    def check_out_and_pay(self, expected_total_price, negative=False):
        checkout_page = CheckoutPage(self.page)
        checkout_page.checkout_and_pay(expected_total_price, negative)

    def on_finish(self):
        self.context.close()
        self.browser.close()


# This part is for running methods directly from the basic page - no need for inheritance and 'child' layer.

# with sync_playwright() as playwright:
#     purchase = Basic
#     purchase.login(playwright)
#     purchase.go_shopping(playwright)
#     purchase.check_out_and_pay(playwright, "£56.99")
#
#     # =====Go Negative =====
#     purchase.go_shopping_neg(playwright)
#     purchase.check_out_and_pay(playwright, "£36.99", True)
