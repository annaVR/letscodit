__author__ = 'anna'
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging
from utilities.messages import *
from traceback import print_stack
import time


class testStatus(SeleniumDriver):

    log = custom_logger(logging.INFO)

    def __init__(self, driver):

        super(testStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, test_name, result):
        try:
            if result is not None:
                if result:
                    self.result_list.append('PASS')
                    self.log.info(verification_successful_message(test_name))
                else:
                    self.result_list.append('FAIL')
                    self.log.error(verification_failed_message(test_name))
                    self.screenshot(test_name)
            else:
                self.result_list.append('FAIL')
                self.log.error(verification_failed_message(test_name))
                self.screenshot(test_name)
        except:
            self.result_list.append('FAIL')
            self.log.error(exception_occurred_message(test_name))
            self.screenshot(test_name)
            print_stack()


    #call on every assertion in the test_case except final assertion
    def mark(self, test_name, result):

        self.set_result(test_name, result)

    # call on final assertion in the test_case
    def mark_final(self, test_funk_name, test_name, result):

        self.set_result(test_name, result)
        print("Result_list:", self.result_list)

        if "FAIL" in self.result_list:
            self.log.error(test_failed_message(test_funk_name))
            self.result_list.clear()
            assert False
        elif 'PASS' in self.result_list:
            self.log.info(test_successful_message(test_funk_name))
            self.result_list.clear()
            assert True
        else:
            self.log.error(test_cannot_collect_message(test_funk_name))
            self.result_list.clear()
            assert False
