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

        if self.browser == "Firefox":
            driver = webdriver.Firefox()
            print('Running on Firefox.')
        else:
            self.browser == 'chrome'
            #driver_location = '/home/anna/bin/chromedriver' # for mac: /Users/anna/bin/chromedriver
            #os.environ['webdriver.chrome.driver'] = driver_location
            # Commented out chromedriver location setup to os.environ because I did set it up in .bash_profile
            driver = webdriver.Chrome()
            driver.set_window_size(3000, 1800)
            print('Running on Chrome.')

        driver.implicitly_wait(6)
        driver.maximize_window()
        driver.get(url)
        return driver
