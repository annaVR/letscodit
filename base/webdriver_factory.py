__author__ = 'anna'

from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser


    def get_web_driver_instance(self):
        url = 'https://letskodeit.teachable.com/'
        # if self.browser == 'iexplorer':
        #     #we need to set IE environment(IE driver) based on OS
        #     driver = webdriver.Ie()
        #     print('Running on IE.')
        if self.browser == 'chrome':
            driver_location = '/home/anna/bin/chromedriver' # for mac: /Users/anna/bin/chromedriver
            os.environ['webdriver.chrome.driver'] = driver_location
            driver = webdriver.Chrome(driver_location)
            print('Running on Chrome.')
        else:
            driver = webdriver.Firefox()
            print('Running on Firefox.')

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(url)
        return driver
