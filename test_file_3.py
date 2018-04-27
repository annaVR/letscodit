__author__ = 'anna'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = 'https://letskodeit.teachable.com/'

# driver_location = '/home/anna/bin/chromedriver'
# os.environ['webdriver.chrome.driver'] = driver_location
# driver = webdriver.Chrome(driver_location)

driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(4)
# driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, '//a[@href="/sign_in"]').click()
time.sleep(3)
driver.find_element(By.ID, 'user_email').send_keys('test@email.com')
driver.find_element(By.ID, 'user_password').send_keys('abcabc')
time.sleep(2)
driver.find_element(By.NAME, 'commit').click()
time.sleep(3)
driver.quit()
