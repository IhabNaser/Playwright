from jproperties import Properties

creds_configs = Properties()

# app-properties
with open('../../Properties/app.properties', 'rb') as config_file:
    creds_configs.load(config_file)

webUrl = creds_configs.get("webUrl").data
password = creds_configs.get("password").data

with open('../../Models/Locators/login_page_locaros.properties', 'rb') as login_locators_file:
    creds_configs.load(login_locators_file)

enter_password = creds_configs.get("enter_password").data
button = creds_configs.get("button").data
enter = creds_configs.get("enter").data
link = creds_configs.get("link").data
shop_all = creds_configs.get("Shop_all").data
banner_template = creds_configs.get("banner_template").data
expected_text = creds_configs.get("expected_text").data

