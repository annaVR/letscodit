__author__ = 'anna'

from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def ClassSetup(self, module_set_up_level_to_test_a_class):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login('test@email.com', 'abcabc')

        # to verify that login successful
        result = self.lp.verify_login_success()
        assert result is True
        result2 = self.lp.verity_title()
        assert result2 is True

    @pytest.mark.run(order=1)
    def test_login_empty_email_empty_password(self):
        self.lp.login()
        result = self.lp.verify_login_failed()
        assert result is True
