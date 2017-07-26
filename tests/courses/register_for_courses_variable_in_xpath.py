__author__ = 'anna'

from pages.courses.register_for_courses_page import RegisterForCourses
import unittest
import pytest
from utilities.test_status import testStatus
import time
from pages.home.navigation_bar import NavigationBar

@pytest.mark.usefulfixture('module_set_up_level_to_test_a_class', 'method_set_up')

class RegisterForCoursesWithXpathVariable(unittest.TestCase):

    @pytest.fixture(autouse=True)

    def object_setup(self, 'module_set_up_level_to_test_a_class'):
        self.reg_for_courses = RegisterForCourses(self.driver)
        self.test_status = testStatus(self.driver)
        self.nav = NavigationBar(self.driver)

    def set_up(self):
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)

    def test_enroll_with_invalid_card(self):
