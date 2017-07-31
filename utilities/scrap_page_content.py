__author__ = 'anna'

import requests
from lxml import html

def get_clean_data(url, xpath):
    page_content = requests.get(url)
    tree = html.fromstring(page_content.content)
    data = tree.xpath(xpath)
    clean_data = [item.strip() for item in data]
    return clean_data

def get_raw_data(url, xpath):
    page_content = requests.get(url)
    tree = html.fromstring(page_content.content)
    data = tree.xpath(xpath)
    return data