#this file should under tests package(uppermost level)
__author__ = 'anna'
import pytest
from selenium import webdriver
import os
from base.webdriver_factory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def method_set_up():
    print('Method setup')
    yield
    print('Method teardown')

# @pytest.fixture(scope='module')
# def module_set_up(browser, os_type):
#     print('Module setup')
#     if browser == 'Firefox':
#         print('Running test on FF')
#     else:
#         print('Running test on Chrome')
#
#     if os_type == 'Linux':
#         print('Running test on Linux')
#     else:
#         print('Running test on OS X')
#     yield
#     print('Module teardown')

@pytest.fixture(scope='class')
def module_set_up_level_to_test_a_class(request, browser):
    print('One time setup.')

    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login('test@email.com', 'abcabc')

    #to pass value to the TestClassDemo2 if class.requests it!! while initializing instance
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print('One time teardown.')

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def os_type(request):
    return request.config.getoption("--osType")


