import logging
import re
import pytest
from playwright.sync_api import sync_playwright
from Common import ExpectedPropsReader
from Tests.Client.Basic import Basic

expected_reader = ExpectedPropsReader


@pytest.mark.only_browser("chromium")
def test_purchase_scenario():
    logging.info("scenario #1 - go shopping and observe behaviour")
    with sync_playwright() as playwright:
        basic = Basic(playwright)
        basic.login()
        basic.go_shopping()
        basic.check_out_and_pay(expected_reader.final_price)
        basic.on_finish()


@pytest.mark.only_browser("chromium")
def test_neg_purchase_scenario():
    logging.info("scenario #2 - go shopping with nge. values and observe behaviour")
    with sync_playwright() as playwright:
        basic = Basic(playwright)
        basic.login()
        basic.go_shopping_neg()
        basic.check_out_and_pay(expected_reader.negative_scenario_final_price, True)
        basic.on_finish()
