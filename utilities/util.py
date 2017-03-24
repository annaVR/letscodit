#all most common utilities should be implemented in this class

import time
import traceback
from utilities.custom_logger import custom_logger
from utilities.messages import *
import logging


class Util(object):

    log = custom_logger(logging.INFO)

    def sleep(self, seconds, message=''):

        #puts the program to wait for the specified period of time
        if message is not None:
            self.log.info(sleep_message(seconds, message))
        try:
            time.sleep(seconds)
        except InterruptedError:
            traceback.print_stack()

    def verify_text_contains(self, actual_text, expected_text):
        self.log.info(actual_text_message(actual_text))
        self.log.info(expected_text_message(expected_text))
        if expected_text.lower() in actual_text.lower():
            self.log.info(verification_successful_message(self.verify_text_contains.__name__))
            return True
        else:
            self.log.info(verification_failed_message(self.verify_text_contains.__name__))
            return False

    def verify_text_match(self, actual_text, expected_text):
        self.log.info(actual_text_message(actual_text))
        self.log.info(expected_text_message(expected_text))
        if expected_text.lower() == actual_text.lower():
            self.log.info(verification_successful_message(self.verify_text_contains.__name__))
            return True
        else:
            self.log.info(verification_failed_message(self.verify_text_contains.__name__))
            return False