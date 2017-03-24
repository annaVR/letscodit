"""
This class contains methods common to all the pages in the application
This class inherits from SeleniumDriver class (our custom class)
This class needs to be inherited by all the page classes
This class should not be used by creating object instances
ex:
class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
from utilities.messages import *

class BasePage(SeleniumDriver):

    def __init__(self, driver):

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, expected_title):

        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, expected_title)
        except:
            self.log.error(failed_to_get_page_title_message(self.verify_page_title.__name__))
            print_stack()
            return False

