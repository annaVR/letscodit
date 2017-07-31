__author__ = 'anna'

from pages.courses.register_for_courses_page import RegisterForCourses
import unittest
import pytest
from utilities.test_status import testStatus
import time
from pages.home.navigation_bar import NavigationBar
from utilities.generate_data import generate_invalid_credit_card

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')

class RegisterForCoursesWithXpathVariable(unittest.TestCase):

    @pytest.fixture(autouse=True)

    def object_setup(self, module_set_up_level_to_test_a_class):
        self.reg_for_courses = RegisterForCourses(self.driver)
        self.test_status = testStatus(self.driver)
        self.nav = NavigationBar(self.driver)

    def set_up(self):
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)

    def test_enroll_with_invalid_card(self):
        courses_names = self.reg_for_courses.scrap_courses_names()
        for title in courses_names:
            self.reg_for_courses.select_course_to_enroll(title)
            time.sleep(1)
            card_number, exp_date, cvc = generate_invalid_credit_card()
            self.reg_for_courses.enroll_course(self, card_number=card_number, exp_date=exp_date, cvc=cvc)
            time.sleep(1)
            result = self.reg_for_courses.verify_card_invalid_error()
            self.test_status.mark_final('test_enroll_with_invalid_card',
                                        self.reg_for_courses.verify_card_invalid_error().__name__,
                                        result)
            self.nav.navigate_to_main_logo()


