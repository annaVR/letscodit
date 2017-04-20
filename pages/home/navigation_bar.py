
from base.base_page import BasePage
from utilities.custom_logger import custom_logger
import logging


class NavigationBar(BasePage):
    # we override log locally to get the LoginPage name in logfile
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _main_logo = "//a[contains(@href, 'http://letskodeit.teachable.com')]"
    _my_courses = "//a[@href='/courses/enrolled']"
    _all_courses = "//a[@href='/courses']"
    _practice = "//a[@href='/pages/practice']"
    _user_icon = "//div[@id='navbar']//li[@class='dropdown']"

    #actions on the elements

    def navigate_to_main_logo(self):
        self.element_click(locator=self._main_logo, locator_type="XPATH")

    def navigate_to_my_courses(self):
        self.element_click(locator=self._my_courses, locator_type="XPATH")

    def navigate_to_all_courses(self):
        self.element_click(locator=self._all_courses, locator_type="XPATH")

    def navigate_to_practice(self):
        self.element_click(locator=self._practice, locator_type="XPATH")

    def navigate_to_user_icon(self):
        user_icon_element = self.wait_for_element\
            (locator=self._user_icon, locator_type="XPATH", timeout=10, poll_frequency=1)
        self.element_click(locator=self._user_icon, locator_type='XPATH')




