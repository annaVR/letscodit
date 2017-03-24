__author__ = 'anna'

from base.base_page import BasePage
from utilities.custom_logger import custom_logger
import logging

class RegisterForCourses(BasePage):

    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):

        super().__init__(driver)
        self.driver = driver

    #locators
    _search_box = "//input[@id='search-courses']"
    _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{}')]"
    _all_courses = "//div[@class='course-listing-title']"
    _enroll_button = "//button[@id='enroll-button-top']"
    _ccard_number_field = "//input[@id='cc_field']"
    _ccard_exp_date_field = "//input[@id='cc-exp']"
    _ccard_cvc_field = "//input[@id='cc_cvc']"
    _verify_cc_button = "//button[@id='verify_cc_btn']"

    _invalid_card_message = "//div[contains(text(), 'The card number is invalid.')][2]"

    #element actions
    def enter_course_to_search(self, course_name):
        self.sendkeys(self._search_box, 'XPATH', course_name)

    def select_course_to_enroll(self, full_course_name):
        self.element_click(self._course.format(full_course_name), 'XPATH')

    def click_enroll_button(self):
        self.element_click(self._enroll_button, 'XPATH')

    def enter_ccard_number(self, card_number):
        self.sendkeys(self._ccard_number_field, 'XPATH', card_number)

    def enter_ccard_exp_date(self, exp_date):
        self.sendkeys(self._ccard_exp_date_field, 'XPATH',exp_date)

    def enter_ccard_cvc(self, cvc):
        self.sendkeys(self._ccard_cvc_field, 'XPATH', cvc)

    def click_verify_ccard_button(self):
        self.element_click(self._verify_cc_button, 'XPATH')

    def enter_credit_card_info(self, card_number='', exp_date='', cvc=''):
        self.enter_ccard_number(card_number)
        self.enter_ccard_exp_date(exp_date)
        self.enter_ccard_cvc(cvc)

    # main
    def enroll_course(self, card_number='', exp_date='', cvc=''):
        self.click_enroll_button()
        self.enter_credit_card_info(card_number, exp_date, cvc)
        self.click_verify_ccard_button()

    #negative test. will return True/False
    #we also want to verify that element not only present but displayed on the page(not hidden)
    def verify_card_invalid_error(self):
        message_element = self.wait_for_element(self._invalid_card_message, timeout= 10,
                                                poll_frequency=5, locator_type='XPATH')
        error = self.is_element_displayed(element=message_element)
        return error

