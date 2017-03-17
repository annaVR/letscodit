__author__ = 'anna'

import inspect
import logging

def CustomLogger(log_level=logging.DEBUG):
    #to explore inspect.stack()
    # stack = (inspect.stack())
    # print(type(stack), len(stack))
    # for item in stack:
    #     print(item)

    #gets the name og the class/ method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    #by default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename='automation.log', mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

# def some_func(logging_level):
#     logger = CustomLogger(logging_level)
#     logger.info('Info message')
#     logger.warn('Warning message')
#
# some_func(logging.INFO)





