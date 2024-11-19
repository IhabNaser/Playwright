# Expected Results - Comparison
# with open('../Properties/expectedProps.properties', 'rb') as config_file:
from Common.PropsReader import expected_configs

with open('../../Models/Locators/shopping_page_locators.properties',
          'rb') as config_file:
    expected_configs.load(config_file)

products = expected_configs.get("products").data
button = expected_configs.get("button").data
burger_page_view = expected_configs.get("burger_page_view").data
product_temp_value = expected_configs.get("product_temp_value").data
item_added = expected_configs.get("item_added").data
open_media= expected_configs.get("open_media").data
product_info_msg= expected_configs.get("product_info_msg").data
your_cart= expected_configs.get("your_cart").data
price_without_shipping= expected_configs.get("price_without_shipping").data
check_out= expected_configs.get("check_out").data
final_price= expected_configs.get("final_price").data
contact= expected_configs.get("contact").data
pay_now_btn= expected_configs.get("pay_now_button").data
header= expected_configs.get("header").data
strong= expected_configs.get("strong").data
confirmation= expected_configs.get("confirmation").data
svg= expected_configs.get("svg").data
order_update= expected_configs.get("order_update").data
paragraph= expected_configs.get("paragraph").data
success_msg= expected_configs.get("success_msg").data
checkout_main= expected_configs.get("checkout_main").data
thank_you_msg= expected_configs.get("thank_you_msg").data
enter_valida_email_msg= expected_configs.get("enter_valida_email_msg").data
negative_scenario_final_price= expected_configs.get("negative_scenario_final_price").data




