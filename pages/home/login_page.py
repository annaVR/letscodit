__author__ = 'anna'

from base.base_page import BasePage
from utilities.custom_logger import custom_logger
from pages.home.navigation_bar import NavigationBar
import logging


class LoginPage(BasePage):
    # we override log locally to get the LoginPage name in logfile
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationBar(self.driver)

    #locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'
    _user_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _sign_out = "//div[@id='navbar']//a[@href='/sign_out']"
    _failed_login_message = "//div[contains(text(),'Invalid email or password')]"

    #actions on the elements
    def click_login_link(self):
        login = self.wait_for_element(locator=self._login_link, locator_type='link', timeout=15)
        self.element_click(locator=self._login_link, locator_type='link')

    def enter_email(self, email):
        email_field = self.wait_for_element(locator=self._email_field, locator_type='id', timeout=15)
        self.sendkeys(email, locator=self._email_field, locator_type='id')

    def enter_password(self, password):
        self.sendkeys(password, locator=self._password_field, locator_type='id')

    def click_login_button(self):
        self.element_click(locator=self._login_button, locator_type='name')

    #main
    #login has optional parameters (to login with empty credentials)

    #since we logged in in setup method by default, we should logout to perform login tests
    def logout(self):
        self.nav.navigate_to_user_icon()
        sign_out = self.wait_for_element(locator=self._sign_out,
                                         locator_type='XPATH')
        self.element_click(locator=self._sign_out,
                                         locator_type='XPATH')


    def login(self, email='', password=''):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        # verify that test is successful if certain element is present on the page
        # will return True or False
    def verify_login_successful(self):
        user_icon = self.is_element_present(locator_type='XPATH', locator=self._user_icon)
        return user_icon

        # will return True or False
    def verify_login_failed(self):
        failure_message = self.is_element_present(locator_type='xpath', locator=self._failed_login_message)
        return failure_message

    def verify_login_title(self):
        return self.verify_page_title("Let's Kode It")




