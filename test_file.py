__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://letskodeit.teachable.com/'
driver = webdriver.Firefox()
print('Running on Firefox.')

driver.implicitly_wait(4)
driver.maximize_window()
driver.get(url)

_login_link = 'Login'
_email_field = 'user_email'
_password_field = 'user_password'
_login_button = 'commit'


driver.find_element(By.LINK_TEXT, _login_link).click()
driver.find_element(By.ID, _email_field).send_keys('test@email.com')
driver.find_element(By.ID, _password_field).send_keys('abcabc')
driver.find_element(By.NAME, _login_button).click()
time.sleep(3)


_user_icon = "//div[@id='navbar']//span[text()='User Settings']"
_signout = "//div[@id='navbar']//a[@href='/sign_out']"
driver.find_element(By.XPATH, _user_icon).click()
driver.find_element(By.XPATH, _signout).click()
time.sleep(2)
driver.quit()