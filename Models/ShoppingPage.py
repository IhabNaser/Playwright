from Models.CheckoutPage import CheckoutPage
from Models.LoginPage import BasicPage, Tabs
from playwright.sync_api import expect


class ShoppingPage(BasicPage):
    """
    Shopping Page - represents the main shopping page model
     methods: <Base>
      1. login
      2. validate_login_success
      3. screenshot
      4. get_creds
      4. checkout
    """

    def __init__(self, pageItem, webUrl):
        super().__init__(pageItem, webUrl)

    def get_burger(self, size, amount=1):
        self.search(self.props_rader.dropit_burger)
        self.validate_product_page()
        self.page.get_by_text(size).click()  # size of burger
        for i in range(1, amount):  # loop over the increase button
            self.increae_amount()

    def dropit_burger_purchase_scenario(self):
        self.navigate_tabs(Tabs.Catalog)
        expect(self.page.locator(self.props_rader.h1)).to_contain_text(self.expected_reader.products)
        self.get_burger(self.props_rader.so_large_burger)
        self.add_to_cart_and_contiune()
        self.get_burger(self.props_rader.medium, 2)
        self.add_to_cart_and_contiune()
        self.validate_expected_bag_value("3")
        self.get_chips(self.props_rader.too_much_chips)
        self.add_to_cart_and_contiune()
        self.get_chips(self.props_rader.large_chips, 2)
        self.add_to_cart_and_contiune()
        self.validate_expected_bag_value("6")
        self.click_card()

    def dropit_neg_scenario(self):
        self.navigate_tabs(Tabs.Catalog)
        expect(self.page.locator(self.props_rader.h1)).to_contain_text(self.expected_reader.products)
        self.get_burger(self.props_rader.so_large_burger)
        self.add_to_cart_and_contiune()
        self.get_chips(self.props_rader.too_much_chips)
        self.add_to_cart_and_contiune()
        self.click_card()

    def get_chips(self, size, amount=1):
        self.search(self.props_rader.dropit_chips)
        self.validate_chips_page()
        self.page.get_by_text(size).click()  # size of chips
        for i in range(1, amount):  # loop over the increase button
            self.increae_amount()

    def increae_amount(self):
        self.page.get_by_role(self.props_rader.button, name=self.props_rader.increase_qnt).click()

    def continue_shopping(self):
        self.page.get_by_role(self.props_rader.button, name=self.props_rader.continue_shopping).click()

    def add_to_cart(self):
        self.page.get_by_role(self.props_rader.button, name=self.props_rader.add_to_cart).click()

    def click_card(self):
        self.page.click("[id='cart-icon-bubble']")

    def add_to_cart_and_contiune(self):
        self.add_to_cart()
        self.validate_item_added()
        self.continue_shopping()

    def validate_product_page(self):
        expect(
            self.page.get_by_role(self.props_rader.button, name=self.expected_reader.burger_page_view)).to_be_visible()
        expect(self.page.locator(self.props_rader.product_temp)).to_contain_text(
            self.expected_reader.product_temp_value)

    def validate_item_added(self):
        expect(self.page.get_by_role(self.props_rader.heading, name=self.expected_reader.item_added)).to_be_visible()

    def validate_expected_bag_value(self, value):
        expect(self.page.locator(self.props_rader.cart_bag)).to_contain_text(value)

    def validate_chips_page(self):
        expect(self.page.get_by_role(self.props_rader.button, name=self.expected_reader.open_media)).to_be_visible()
        expect(self.page.locator(self.props_rader.product_info_temp)).to_contain_text(
            self.expected_reader.product_info_msg)
