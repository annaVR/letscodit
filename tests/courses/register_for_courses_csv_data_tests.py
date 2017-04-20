
from pages.courses.register_for_courses_page import RegisterForCourses
import unittest
import pytest
from utilities.test_status import testStatus
import time
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
from pages.home.navigation_bar import NavigationBar

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')
@ddt
class RegisterCoursesCSVDataTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, module_set_up_level_to_test_a_class):
        self.reg_for_courses = RegisterForCourses(self.driver)
        self.test_status = testStatus(self.driver)
        self.nav = NavigationBar(self.driver)

    def set_up(self):

        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    # * asterisk below is to unpack list
    @data(*get_csv_data('/home/anna/PycharmProjects/letscodit/test_data.csv'))
    @unpack
    def test_enroll_with_invalid_card(self, course_name, cc_number, cc_exp, cc_cvc):

        self.reg_for_courses.enter_course_to_search(course_name)
        self.reg_for_courses.select_course_to_enroll(course_name)
        time.sleep(1)
        self.reg_for_courses.enroll_course(card_number=cc_number, exp_date=cc_exp, cvc=cc_cvc)
        time.sleep(1)
        result = self.reg_for_courses.verify_card_invalid_error()
        self.test_status.mark_final('test_enroll_with_invalid_card',
                                    self.reg_for_courses.verify_card_invalid_error.__name__, result)

        self.nav.navigate_to_main_logo()