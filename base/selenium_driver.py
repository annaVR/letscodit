__author__ = 'anna'


from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.messages import *
from utilities.custom_logger import custom_logger
import logging
import time
import datetime
import os

class SeleniumDriver():

    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, test_name):
        """
        takes screenshot of a current open web page
        """
        time_stamp = time.time()
        time_stamp_string = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y%m%d:%H:%M:%S')
        file_name = "{}.{}.png".format(test_name, time_stamp_string)
        relative_screenshot_directory = '../screenshots/'
        relative_file_path= '{}{}'.format(relative_screenshot_directory, file_name)
        current_directory = os.path.dirname(__file__)
        destination_file_path = os.path.join(current_directory, relative_file_path)
        destination_directory = os.path.join(current_directory, relative_screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file_path)
            self.log.info(screenshot_saved_message(test_name, destination_file_path))
        except:
            self.log.error(screenshot_exception_occurred_message(test_name, destination_file_path))
            print_stack()



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
            self.log.info(locator_error_message(locator_type))
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

    def get_element_list(self, locator, locator_type='id'):
        elements_list = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements_list = self.driver.find_elements(by_type, locator)
            self.log.info(elements_list_found_message(locator_type, locator))
        except:
            self.log.info(elements_list_not_found_message(locator_type, locator))
        return elements_list

    # do not use element keyword argument - it is not working properly.
    # use only locator/locator_type kwargs
    def element_click(self, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(element_clicked_message(locator_type, locator))
        except:
            self.log.info(element_not_clicked_message(locator_type, locator))
            self.log.info(print_stack())

     # do not use element keyword argument - it is not working properly.
    # use only locator/locator_type kwargs
    def sendkeys(self, keys, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(keys)
            self.log.info(element_send_keys_message(locator_type, locator, keys))
        except:
            self.log.info(element_cannot_send_keys_message(locator_type, locator,keys))
            self.log.info(print_stack())

     # do not use element keyword argument - it is not working properly.
    # use only locator/locator_type kwargs
    def get_text(self, locator='', locator_type='id', element=None, info=''):

        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

     # do not use element keyword argument - it is not working properly.
    # use only locator/locator_type kwargs
    def is_element_present(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present. Locator_type: {}, locator: {}.".format(locator_type, locator))
                return True
            else:
                self.log.info("Element not present. Locator_type: {}, locator: {}.".format(locator_type, locator))
                return False
        except:
            self.log.info(element_not_found_message(locator_type, locator))
            return False

     # do not use element keyword argument - it is not working properly.
    # use only locator/locator_type kwargs
    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed. Locator_type: {}, locator: {}.".format(locator_type, locator))
            else:
                self.log.info("Element is not displayed. Locator_type: {}, locator: {}.".format(locator_type, locator))
            return is_displayed
        except:
            self.log.info(element_not_found_message(locator_type, locator))
            return False

    def wait_for_element(self, locator, locator_type='id',
                         timeout=10, poll_frequency=1):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(waiting_message(locator_type, locator, timeout))
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info(element_appeared_message(locator_type, locator))
            return element
        except:
            self.log.info(element_not_appeared_message(locator_type, locator))
            self.log.info(print_stack())
        return element

    def web_scroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        elif direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")






