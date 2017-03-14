__author__ = 'anna'

from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_link = self.driver.find_element(By.LINK_TEXT, 'Login')
        login_link.click()

        email_field = self.driver.find_element(By.ID, 'user_email')
        email_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, 'user_password')
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.NAME, 'commit')
        login_button.click()
