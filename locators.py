from selenium.webdriver.common.by import By
class MyAccountLocators:
    accept_rodo = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    register = (By.XPATH, "//a[@href='/user/register']")
    email_input= (By.XPATH, "//input[@id='edit-mail']")
    password_input = (By.XPATH, "//input[@id='edit-pass-pass1']")
    password_repetition_input = (By.XPATH, "//input[@id='edit-pass-pass2']")
    data_protection = (By.XPATH, "//input[@id='edit-field-u-regulations-und']")
    captcha = (By.XPATH, "//div[@class='recaptcha-checkbox-borderAnimation']")
    button = (By.XPATH, "//button[@id='edit-submit']")
    error_message = (By.XPATH, "//div[@class='messages error alert alert-block alert-error fade in']")

class LogInLocators:
    accept_rodo = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    login = (By.XPATH, "//a[@href='/user/login']")
    email_input_login = (By.XPATH, "//input[@id='edit-name']")
    password_input_login = (By.XPATH, "//input[@id='edit-pass']")
    button_login = (By.XPATH, "//button[@id='edit-submit']")
    error_message = (By.XPATH, "//div[@class='messages error alert alert-block alert-error fade in']")

class SearchLocators:
    search = (By.XPATH, "//input[@placeholder='szukaj produktu, autora...']")
    order = (By.XPATH, "//*[@id='block-system-main']/div/div/ol/li[3]/div[2]/div[1]/h4/a")
    basket = (By.XPATH, "//button[@id='edit-submit']")
    go_to_basket = (By.XPATH, "//*[@id='block-system-main']/div[1]/div/div/div[3]/div[2]/a")
    order_submit = (By.XPATH, "//button[@id='edit-checkout']")
    phone_input = (By.XPATH, "//input[@id='edit-account-login-phone']")
    name_input = (By.XPATH, "//input[@id='edit-customer-profile-shipping-commerce-customer-address-und-0-name-line']")
    address_input =(By.XPATH, "//input[@id='edit-customer-profile-shipping-commerce-customer-address-und-0-thoroughfare']")
    zip_code_input =(By.XPATH, "//input[@id='edit-customer-profile-shipping-commerce-customer-address-und-0-postal-code']")
    place_input =(By.XPATH, "//input[@id='edit-customer-profile-shipping-commerce-customer-address-und-0-locality']")
    saved_addresses_input = (By.XPATH, "//option[@value='1324500']")
    payment_method_input = (By.XPATH, "//button[@id='edit-continue']")
