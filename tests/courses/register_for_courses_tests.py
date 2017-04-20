__author__ = 'anna'

from selenium import webdriver
from pages.courses.register_for_courses_page import RegisterForCourses
import unittest
import pytest
from utilities.test_status import testStatus
import time

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, module_set_up_level_to_test_a_class):
        self.reg_for_courses = RegisterForCourses(self.driver)
        self.test_status = testStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_enroll_with_invalid_card(self):

        self.reg_for_courses.enter_course_to_search('JavaScript')
        self.reg_for_courses.select_course_to_enroll('JavaScript for beginners')
        time.sleep(3)
        self.reg_for_courses.enroll_course(5454, 14, 57)
        time.sleep(3)
        result = self.reg_for_courses.verify_card_invalid_error()
        self.test_status.mark_final(self.test_enroll_with_invalid_card.__name__,
                                    self.reg_for_courses.verify_card_invalid_error.__name__, result)
