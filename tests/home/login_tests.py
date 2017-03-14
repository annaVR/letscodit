__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url)

        lp = LoginPage(driver)
        lp.login('test@email.com', 'abcabc')

        # to verify that login successful
        user_icon = driver.find_element(By.XPATH, "//div[@id='navbar']//span[text()='User Settings']")
        driver.quit()

        if user_icon:
            print('Login successful')
        else:
            print('Login failed')



