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

    def element_click(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(element_clicked_message(locator_type, locator))
        except:
            self.log.info(element_not_clicked_message(locator_type, locator))
            self.log.info(print_stack())

    def sendkeys(self, locator, locator_type, keys):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(keys)
            self.log.info(element_send_keys_message(locator_type, locator, keys))
        except:
            self.log.info(element_cannot_send_keys_message(locator_type, locator,keys))
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
            self.log.info(element_appeared_message(locator_type, locator))
            return element
        except:
            self.log.info(element_not_appeared_message())
            self.log.info(print_stack())






