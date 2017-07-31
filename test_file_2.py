__author__ = 'anna'

# extract name of the courses

import requests
from lxml import html
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

courses_page = requests.get('https://letskodeit.teachable.com/courses')

tree = html.fromstring(courses_page.content)
java_course = tree.xpath("//div[@data-course-id ='56738']//div[@class='course-listing-title']//text()")

all_courses = tree.xpath("//div[@class='course-listing-title']//text()")
print(all_courses)

# titles = []
# for item in all_courses:
#     name = item.strip()
#     titles.append(name)
# print(titles)

url = 'https://letskodeit.teachable.com/courses'
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(4)
driver.maximize_window()
time.sleep(3)

for title in all_courses:
    driver.find_element(By.XPATH, "//div[@class='course-listing-title'and text()='{}' ]".format(title)).click()
    print(title)
    time.sleep(2)
    print(driver.current_url)
    driver.execute_script("window.history.go(-1)")
    print(driver.current_url)

driver.quit()
