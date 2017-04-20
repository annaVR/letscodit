
from selenium import webdriver
from pages.courses.register_for_courses_page import RegisterForCourses
import unittest
import pytest
from utilities.test_status import testStatus
import time
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')
@ddt
class RegisterMultipleCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, module_set_up_level_to_test_a_class):
        self.reg_for_courses = RegisterForCourses(self.driver)
        self.test_status = testStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(('JavaScript for beginners', '5454', '14', '57'), ('Learn Python 3 from scratch', '20', '20', '20'))
    @unpack
    def test_enroll_with_invalid_card(self, course_name, cc_number, cc_exp, cc_cvc):

        self.reg_for_courses.enter_course_to_search(course_name)
        self.reg_for_courses.select_course_to_enroll(course_name)
        time.sleep(3)
        self.reg_for_courses.enroll_course(card_number=cc_number, exp_date=cc_exp, cvc=cc_cvc)
        time.sleep(3)
        result = self.reg_for_courses.verify_card_invalid_error()
        self.test_status.mark_final('test_enroll_with_invalid_card',
                                    self.reg_for_courses.verify_card_invalid_error.__name__, result)
        self.driver.find_element(By.XPATH, "//a[contains(@href, 'http://letskodeit.teachable.com')]").click()
        self.driver.find_element(By.XPATH, "//a[@href='/courses']").click()