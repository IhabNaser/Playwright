from Common import LoginCredsReader, PropsReader, ExpectedPropsReader
from Models.LoginPage import BasicPage
# from playwright.sync_api import expect
from playwright.sync_api import expect


class CheckoutPage:
    """
    Checkout Page - represents the checkout and payment page
     methods: <Base>
      1. checkout_and_pay
      2. checkout
      3. fill_all_fields
      4. fill_personal_info
      5. fill_credit_card_props
      6. validate_payment_success
"""

    def __init__(self, page_item):
        self.login_creds_reader = LoginCredsReader
        self.props_rader = PropsReader
        self.expected_reader = ExpectedPropsReader
        self.page = page_item

    def checkout_and_pay(self, expected_total_price, negative=False):
        self.checkout_form(expected_total_price)
        if negative:
            self.fill_all_fields_neg()
            self.validate_failure()
        else:
            self.fill_all_fields()
            self.validate_payment_success()

    def checkout_form(self, expected_total_price):
        self.page.get_by_role(self.props_rader.button, name=self.props_rader.check_out).click()
        self.validate_checkout_values(expected_total_price)

    def fill_all_fields(self):
        self.fill_personal_info(self.props_rader.phone, self.props_rader.first_name_value,
                                self.props_rader.last_name_value, self.props_rader.address_val,
                                self.props_rader.city_val)
        self.fill_credit_card_props(self.props_rader.card_number, self.props_rader.exp_date, self.props_rader.sec_code,
                                    self.props_rader.name_on_card)
        self.pay_now()

    def fill_all_fields_neg(self):
        self.fill_personal_info(self.props_rader.corrupted_email, self.props_rader.first_name_value,
                                self.props_rader.last_name_value, self.props_rader.address_val,
                                self.props_rader.city_val)
        self.fill_credit_card_props(self.props_rader.wrong_card_number, self.props_rader.exp_date,
                                    self.props_rader.sec_code,
                                    self.props_rader.name_on_card)
        self.pay_now()

    def fill_personal_info(self, phone, first_name, last_name, address, city):
        self.set_email_phone(phone)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_city(city)

    def set_email_phone(self, value):
        self.page.get_by_placeholder(self.props_rader.email_place_holder).fill(value)

    def set_first_name(self, name):
        self.page.get_by_placeholder(self.props_rader.first_name).fill(name)

    def set_last_name(self, last_name):
        self.page.get_by_placeholder(self.props_rader.last_name).fill(last_name)

    def set_address(self, address):
        self.page.get_by_placeholder(self.props_rader.address).fill(address)

    def set_city(self, city):
        self.page.get_by_placeholder(self.props_rader.city).fill(city)

    def validate_checkout_page(self):
        expect(self.page.locator(self.props_rader.cart_items)).to_contain_text(self.expected_reader.your_cart)
        expect(self.page.locator(self.props_rader.cart_footer)).to_contain_text(
            self.expected_reader.price_without_shipping)
        expect(self.page.get_by_role(self.props_rader.button, name=self.expected_reader.check_out)).to_be_visible()

    def validate_checkout_values(self, value):
        expect(self.page.get_by_role(self.props_rader.strong)).to_contain_text(value)
        expect(self.page.get_by_role(self.props_rader.heading, name=self.expected_reader.contact)).to_be_visible()

    def fill_credit_card_props(self, card_num, exp_date, sec_code, card_holder):
        self.set_cc_number(card_num)
        self.set_cc_exp_date(exp_date)
        self.set_cc_sec_code(sec_code)
        self.set_card_holder_name(card_holder)

    def set_cc_number(self, number):
        self.page.locator("iframe[title=\"Field container for: Card number\"]").content_frame.get_by_placeholder(
            self.props_rader.card_num_key).fill(number)

    def set_cc_exp_date(self, exp_date):
        self.page.locator(
            "iframe[title=\"Field container for: Expiration date (MM / YY)\"]").content_frame.get_by_placeholder(
            self.props_rader.exp_date_key).fill(exp_date)

    def set_cc_sec_code(self, sec_code):
        self.page.locator("iframe[title=\"Field container for: Security code\"]").content_frame.get_by_placeholder(
            self.props_rader.sec_code_key).fill(sec_code)

    def set_card_holder_name(self, name):
        self.page.get_by_label(self.props_rader.clear).click()
        self.page.locator("iframe[title=\"Field container for: Name on card\"]").content_frame.get_by_placeholder(
            self.props_rader.name_on_card_key).fill(name)

    def pay_now(self):
        expect(
            self.page.get_by_role(self.props_rader.button, name=self.expected_reader.pay_now_btn)).to_be_visible()
        self.page.get_by_role(self.props_rader.button, name=self.expected_reader.pay_now_btn).click()

    def validate_payment_success(self):
        expect(
            self.page.locator(self.expected_reader.header).filter(has_text=self.expected_reader.confirmation).locator(
                self.expected_reader.svg)).to_be_visible()
        expect(self.page.get_by_role(self.expected_reader.strong)).to_contain_text(self.expected_reader.final_price)
        expect(self.page.get_by_label(self.expected_reader.order_update).get_by_role(
            self.expected_reader.paragraph)).to_contain_text(self.expected_reader.success_msg)
        expect(self.page.locator(self.expected_reader.checkout_main)).to_contain_text(
            self.expected_reader.thank_you_msg)

    def validate_failure(self):
        expect(self.page.get_by_text(self.props_rader.enter_valid_email)).to_be_visible()
        expect(self.page.locator(self.props_rader.error_for_email)).to_contain_text(
            self.expected_reader.enter_valida_email_msg)
