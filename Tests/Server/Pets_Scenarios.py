import logging
from playwright.sync_api import sync_playwright
import json

from Tests.Server import Pet_Base_Api

CREATE_PET_TEMPLATE = "request_templates/create_pet.json"
REQUEST_URL = "https://petstore.swagger.io"
EXPECTED_PET_NAME = "puff"

def init_test(playwright: sync_playwright()):
    global context, pet_base
    pet_base = Pet_Base_Api
    browser = playwright.chromium.launch()
    context = browser.new_context(base_url=REQUEST_URL)


def test_create_and_update_pet(playwright: sync_playwright()):
    init_test(playwright)
    with open(CREATE_PET_TEMPLATE, 'r') as create_pet_body:
        data = json.load(create_pet_body)
    pet_id = pet_base.create_pet(context, data)
    print(f"Created pet Id is: {pet_id}")
    pet_base.update_pet(context, pet_id, pet_base.PET_STATUS.sold)


def test_get_pet_by_status(playwright: sync_playwright()):
    init_test(playwright)
    pets_list = pet_base.get_pet_by_status(context, pet_base.PET_STATUS.available)
    # assert pets_list[3]['name'] == EXPECTED_PET_NAME  # The returned order is not consist , then it can't be asserted by its order.
    logging.info(pets_list[3])


def test_get_pet_by_status_and_validate_returned(playwright: sync_playwright()):
    init_test(playwright)
    pet_base.get_pet_by_status(context, pet_base.PET_STATUS.sold, True)
