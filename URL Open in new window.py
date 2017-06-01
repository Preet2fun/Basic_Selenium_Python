__author__ = 'Pratik'

from selenium import webdriver
driver = webdriver.Firefox()
url='https://www.amazon.com/gp/gw/ajax/s.html'
driver.get(url)

browser = webdriver.Firefox()
url='https://www.google.com'
browser.get(url)