__author__ = 'anna'

from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging


class LoginPage(SeleniumDriver):
    # we override log locally to get the LoginPage name in logfile
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    #actions on the elements
    def click_login_link(self):
        self.element_click(self._login_link, 'link')

    def enter_email(self, email):
        self.sendkeys(self._email_field, 'id', email)

    def enter_password(self, password):
        self.sendkeys(self._password_field, 'id', password)
    def click_login_button(self):
        self.element_click(self._login_button, 'name')

    #main
    #login has optional parameters (to login with empty credentials)
    def login(self, email='', password=''):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        # verify that test is successful if certain element is present on the page
        # will return True or False
    def verify_login_successful(self):
        user_icon = self.is_element_present('XPATH', "//div[@id='navbar']//span[text()='User Settings']")
        return user_icon

        # will return True or False
    def verify_login_failed(self):
        failure_message = self.is_element_present('xpath', "//div[contains(text(), 'Invalid email or password')]")
        return failure_message

    def verify_title(self):
        if "Google" in self.get_title():
            return True
        else:
            return False



