import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from base import BasePageMethods
from locators import MyAccountLocators
from locators import LogInLocators
from locators import SearchLocators

class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.methods = BasePageMethods(self)
        self.MyAccountLocators = MyAccountLocators()
        self.LogInLocators = LogInLocators()
        self.SearchLocators = SearchLocators()

    def open_page(self):
        self.driver.get("https://wydawnictwowam.pl/")
        self.methods.find_element(*self.MyAccountLocators.accept_rodo).click()

    @allure.step("Create account ")
    def create_account(self, email, pass1, pass2):
        self.methods.find_element(*self.MyAccountLocators.register).click()
        self.methods.find_element(*self.MyAccountLocators.email_input).send_keys(email)
        self.methods.find_element(*self.MyAccountLocators.password_input).send_keys(pass1)
        self.methods.find_element(*self.MyAccountLocators.password_repetition_input).send_keys(pass2)
        self.methods.find_element(*self.MyAccountLocators.data_protection).click()
        self.logger.info("Creating account ...".format(email, pass1, pass2))
        allure.attach(self.driver.get_screenshot_as_png(), name="Create account", attachment_type=AttachmentType.PNG)


    @allure.step("Button click ")
    def button_click(self):
        self.methods.find_element(*self.MyAccountLocators.button).click()
        self.logger.info("Clicking button ...".format())
        allure.attach(self.driver.get_screenshot_as_png(), name="Button click", attachment_type=AttachmentType.PNG)

    @allure.step("login account ")
    def login_account(self, email, password):
        self.methods.find_element(*self.LogInLocators.login).click()
        self.methods.find_element(*self.LogInLocators.email_input_login).send_keys(email)
        self.methods.find_element(*self.LogInLocators.password_input_login).send_keys(password)
        self.methods.find_element(*self.LogInLocators.button_login).click()
        self.logger.info("Login account ...".format(email, password))
        allure.attach(self.driver.get_screenshot_as_png(), name="Login account", attachment_type=AttachmentType.PNG)

    @allure.step("Error message ")
    def get_error_message(self):
        return self.methods.find_element(self.LogInLocators.error_message).text
        self.logger.info("Error message ...".format())
        allure.attach(self.driver.get_screenshot_as_png(), name="Error message ", attachment_type=AttachmentType.PNG)

    @allure.step("Search account ")
    def search_account(self, name):
        self.methods.find_element(*self.SearchLocators.search).send_keys(name)
        self.methods.find_element(*self.SearchLocators.search).send_keys(Keys.ENTER)
        self.methods.find_element(*self.SearchLocators.order).click()
        self.methods.find_element(*self.SearchLocators.basket).click()
        self.methods.find_element(*self.SearchLocators.go_to_basket).click()
        self.logger.info("Searching account".format(name))
        allure.attach(self.driver.get_screenshot_as_png(), name="Search account ", attachment_type=AttachmentType.PNG)

    @allure.step("Submit order ")
    def submit_order_account(self, phone, name, address, zip_code, place):
        self.methods.find_element(*self.SearchLocators.order_submit).click()
        self.methods.find_element(*self.SearchLocators.phone_input).send_keys(phone)
        self.methods.find_element(*self.SearchLocators.name_input).send_keys(name)
        self.methods.find_element(*self.SearchLocators.address_input).send_keys(address)
        self.methods.find_element(*self.SearchLocators.zip_code_input).send_keys(zip_code)
        self.methods.find_element(*self.SearchLocators.place_input).send_keys(place)
        self.methods.find_element(*self.SearchLocators.saved_addresses_input).click()
        self.methods.find_element(*self.SearchLocators.payment_method_input).click()
        self.logger.info("Submitting order ...".format(phone, name, address, zip_code, place))
        allure.attach(self.driver.get_screenshot_as_png(), name="Submit order ", attachment_type=AttachmentType.PNG)


    @allure.step("Submit order ")
    def submit_order_account(self, phone, name, address, zip_code, place):
        self.methods.find_element(*self.SearchLocators.order_submit).click()
        self.logger.info("Submitting order ...".format(phone, name, address, zip_code, place))