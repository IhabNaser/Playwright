import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from Common import ExpectedPropsReader
from Tests.Client.Basic import Basic


class PurchaseTest(Basic):
    def __init__(self):
        global loginPage, classInstance
        super().__init__()
        self.expected_reader = ExpectedPropsReader

    @pytest.mark.only_browser("chromium")
    def test_purchase_scenario(self):
        self.login()
        self.go_shopping()
        self.check_out_and_pay(self.expected_reader.final_price)
        self.on_finish()

    @pytest.mark.only_browser("chromium")
    def test_neg_purchace_scenario(self):
        self.login()
        self.go_shopping_neg()
        self.check_out_and_pay(self.expected_reader.negative_scenario_final_price, True)
        self.on_finish()
