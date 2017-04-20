import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_for_courses_csv_data_tests import RegisterCoursesCSVDataTest


# get all tests from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTest)

smoke_test= unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
