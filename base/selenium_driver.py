__author__ = 'anna'


from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.messages import *
from utilities.custom_logger import CustomLogger
import logging

class SeleniumDriver():

    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info(locator_error(locator_type))
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(element_found_message(by_type, locator))
        except:
            self.log.info(element_not_found_message(by_type, locator))
        return element

    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(element_clicked(locator_type, locator))
        except:
            self.log.info(element_not_clicked(locator_type, locator))
            self.log.info(print_stack())

    def sendkeys(self, locator, locator_type, keys):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(keys)
            self.log.info(element_send_keys(locator_type, locator, keys))
        except:
            self.log.info(element_not_send_keys(locator_type, locator,keys))
            self.log.info(print_stack())


    def is_element_present(self, locator_type, locator):
        try:
            element = self.get_element(locator, locator_type)
            return True
        except:
            return False

    def wait_for_element(self, locator, timeout, poll_frequency,locator_type='id'):
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(waiting_message(locator_type, locator, timeout))
            wait = WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                                                           ElementNotVisibleException,
                                                                                           ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            self.log.info(element_appeared(locator_type, locator))
            return element
        except:
            self.log.info(element_not_appeared())
            self.log.info(print_stack())






