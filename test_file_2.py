__author__ = 'anna'

# extract name of the courses

import requests
from lxml import html

from selenium import webdriver
from selenium.webdriver.common.by import By


courses_page_content = requests.get('https://letskodeit.teachable.com/courses')

# tree = html.fromstring(courses_page_content)
tree = etree
java_course = tree.xpath("//div[@data-course-id ='56738']//div[@class='course-listing-title']//text()")

print(java_course)
