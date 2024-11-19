from jproperties import Properties

props_configs = Properties()
expected_configs = Properties()

# app-properties
with open('../../Models/Locators/shopping_page_locators.properties',
          'rb') as config_file:
    props_configs.load(config_file)

# webUrl = props_configs.get("webUrl").data
h1 = props_configs.get("h1").data
link = props_configs.get("link").data
button = props_configs.get("buttonSetter").data
screenshotsPath = props_configs.get("screenshotsPath").data
search = props_configs.get("search").data
product_temp = props_configs.get("product_temp").data
dropit_burger = props_configs.get("dropit_burger").data
dropit_chips = props_configs.get("dropit_chips").data
card_number = props_configs.get("card_number").data
exp_date = props_configs.get("exp_date").data
sec_code = props_configs.get("sec_code").data
clear = props_configs.get("clear").data
name_on_card = props_configs.get("name_on_card").data
add_to_cart = props_configs.get("add_to_cart").data
continue_shopping = props_configs.get("continue_shopping").data
so_large_burger = props_configs.get("so_large_burger").data
medium = props_configs.get("medium").data
increase_qnt = props_configs.get("increase_qnt").data
heading = props_configs.get("heading").data
cart_bag = props_configs.get("cart_bag").data
product_info_temp = props_configs.get("product_info_temp").data
too_much_chips = props_configs.get("too_much_chips").data
large_chips = props_configs.get("large_chips").data
latest_card_value = props_configs.get("latest_card_value").data
cart_items = props_configs.get("cart_items").data
cart_footer = props_configs.get("cart_footer").data
check_out = props_configs.get("check_out").data
strong = props_configs.get("strong").data
webUrl = props_configs.get("webUrl").data
email_place_holder = props_configs.get("email_place_holder").data
first_name = props_configs.get("first_name").data
last_name = props_configs.get("last_name").data
address = props_configs.get("address").data
city = props_configs.get("city").data
phone = props_configs.get("phone").data
first_name_value = props_configs.get("first_name_value").data
last_name_value = props_configs.get("last_name_value").data
city_val = props_configs.get("city_val").data
address_val = props_configs.get("address_val").data
card_num_key = props_configs.get("card_num_key").data
exp_date_key = props_configs.get("exp_date_key").data
sec_code_key = props_configs.get("sec_code_key").data
name_on_card_key = props_configs.get("name_on_card_key").data
corrupted_email = props_configs.get("corrupted_email").data
wrong_card_number = props_configs.get("wrong_card_number").data
enter_valid_email = props_configs.get("enter_valid_email").data
error_for_email = props_configs.get("error_for_email").data
icon_cart = props_configs.get("icon_cart").data
cart_icon_bubble = props_configs.get("cart_icon_bubble").data
