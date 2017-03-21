__author__ = 'anna'

from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.test_status import testStatus

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def ClassSetup(self, module_set_up_level_to_test_a_class):
        self.lp = LoginPage(self.driver)
        self.test_status = testStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login_and_title(self):

        # these verifications are mixed in one test in order
        # to test testStatus class -multiple assertions in 1 test:

        # to verify_title - we are verifying false statement title contains 'Google'
        # in order to get False as a result, because we need the first assertion here fail
        result = self.lp.verify_title()
        self.test_status.mark(self.lp.verify_title.__name__, result)

        # to verify that login successful
        self.lp.login('test@email.com', 'abcabc')
        result2 = self.lp.verify_login_successful()
        self.test_status.mark_final(self.test_valid_login_and_title.__name__,
                                    self.lp.verify_login_successful.__name__, result2)

    @pytest.mark.run(order=1)
    def test_login_empty_email_empty_password(self):
        self.lp.login()
        result = self.lp.verify_login_failed()
        self.test_status.mark_final(self.test_login_empty_email_empty_password.__name__,
                                    self.lp.verify_login_failed.__name__, result)