import time
import locators
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePageMethods(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locators):
        self.wait.until(EC.presence_of_element_located(locators))
        return self.driver.find_element(*locators)

    def find_elements(self, *locators):
        self.wait.until(EC.visibility_of_all_elements_located(locators))
        return self.driver.find_elements(*locators)

    def clear_input(self, *locators):
        self.driver.find_element(*locators).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*locators).send_keys(Keys.DELETE)

    def clear_input(self, *locators):
        self.driver.find_element(*locators).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*locators).send_keys(Keys.DELETE)
        # self.driver.find_element(*locators).clear()

    def fill_text_field(self, value, *locators):
        self.click_button(*locators)
        elem = self.find_element(*locators)
        elem.send_keys(value)

    def fill_text_field_dropdown(self, value, *locators):
        self.click_button_click(*locators)
        elem = self.find_element(*locators)
        elem.send_keys(value)
        elem.send_keys(Keys.ENTER)
    def click_button(self, *locators):
        self.wait.until(EC.visibility_of_element_located(locators))
        self.wait.until(EC.element_to_be_clickable(locators))
        element = self.find_element(*locators)
        self.driver.execute_script("arguments[0].click();", element)

    def click_button_in_frame(self, *locator):
        iframe = self.driver.find_element(By.XPATH, GeneralLocators.IFrameLocator)
        self.driver.switch_to.frame(iframe)
        self.find_element(*locator).click()
        self.driver.switch_to.default_content()

    def check_visible_result_in_frame(self, *locators):
        iframe = self.driver.find_element(By.XPATH, GeneralLocators.IFrameLocator)
        self.driver.switch_to.frame(iframe)
        self.wait.until(EC.visibility_of_element_located(locators))
        text = self.find_element(*locators).text
        self.driver.switch_to.default_content()
        return text

    def fill_text_field_in_frame(self, value, *locators):
        iframe = self.driver.find_element(By.XPATH, GeneralLocators.IFrameLocator)
        self.driver.switch_to.frame(iframe)
        self.fill_text_field(value, *locators)
        self.driver.switch_to.default_content()

    def click_button_click(self, *locators):
        self.wait.until(EC.visibility_of_element_located(locators))
        self.wait.until(EC.element_to_be_clickable(locators))
        self.find_element(*locators).click()

    def time_count(self, timeDelay):
        time = datetime.now().strftime('%H:%M:%S')
        time_string = str(time)
        date = datetime.strptime(time_string, '%H:%M:%S')
        minutesPlus = date + timedelta(minutes=timeDelay)
        return str(minutesPlus)[11:]

    def hour_count(self, timeDelay):
        time = datetime.now().strftime('%H:%M:%S')
        time_string = str(time)
        date = datetime.strptime(time_string, '%H:%M:%S')
        minutesPlus = date + timedelta(hours=timeDelay)
        return str(minutesPlus)[11:]

    def check_visible_result(self, *locators):
        self.wait.until(EC.visibility_of_element_located(locators))
        return self.find_element(*locators).text

    def check_visible_result_with_value(self, path):
        locator = (By.XPATH, path)
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.find_element(*locator).text

    def check_visible_value(self, *locators):
        self.wait.until(EC.visibility_of_element_located(locators))
        return self.find_element(*locators).get_attribute('value')

    def is_not_located(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))
        time.sleep(1)

    def clear_input_in_frame(self, *locators):
        iframe = self.driver.find_element(By.XPATH, GeneralLocators.IFrameLocator)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*locators).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*locators).send_keys(Keys.DELETE)
        self.driver.switch_to.default_content()

    def find_element_in_frame(self, *locators):
        iframe = self.driver.find_element(By.XPATH, GeneralLocators.IFrameLocator)
        self.driver.switch_to.frame(iframe)
        self.wait.until(EC.presence_of_element_located(locators))
        element = self.driver.find_element(*locators)
        #self.driver.switch_to.default_content()
        return element
