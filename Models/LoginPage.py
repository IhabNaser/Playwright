import logging
import re
from enum import Enum
from playwright.async_api import expect
import datetime

from Common import LoginCredsReader, PropsReader, ExpectedPropsReader


class Tabs(Enum):
    Home = 1
    Catalog = 2
    Contact = 3
    Search = 4


class BasicPage:
    """
    Basic Page - represents a base page for all pages in the project
     methods:
      1. login
      2. validate_login_success
      3. screenshot
      4. get_creds
    """

    def __init__(self, pageItem, webUrl):
        self.page = pageItem
        self.page.goto(webUrl)
        self.login_creds_reader = LoginCredsReader
        self.props_rader = PropsReader
        self.expected_reader = ExpectedPropsReader

    def login(self):
        password = self.get_creds()
        logging.info("login password is: " + password)
        self.page.get_by_label(self.login_creds_reader.enter_password).fill(password)
        self.page.get_by_role(self.login_creds_reader.button, name=self.login_creds_reader.enter).click()
        self.screenshot()
        # self.validate_login_success()

    def validate_login_success(self):
        expect(self.page.locator(self.login_creds_reader.banner_template)).to_contain_text(
            self.login_creds_reader.expected_text)
        expect(
            self.page.get_by_role(self.login_creds_reader.link, name=self.login_creds_reader.shop_all)).to_be_visible()

    def screenshot(self):
        now = datetime.datetime.now()
        filename = now.strftime("%Y-%m-%d-%H-%M-%S") + '.png'
        full_file_name = self.props_rader.screenshotsPath + '/' + filename
        logging.info("Taking a snap as screenshot in :" + full_file_name)
        return self.page.screenshot(path=full_file_name)

    def get_creds(self):
        return self.login_creds_reader.password

    def navigate_tabs(self, tab: Tabs = Tabs.Catalog):
        self.page.get_by_role(self.login_creds_reader.link, name=tab.name).click()

    def search(self, value):
        self.page.get_by_role(self.props_rader.button, name=self.props_rader.search).click()
        self.page.get_by_placeholder(self.props_rader.search).fill(value)
        self.page.get_by_role(self.props_rader.link, name=value).click()
