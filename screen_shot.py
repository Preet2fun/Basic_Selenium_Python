__author__ = 'Pratik'

from selenium import webdriver
driver = webdriver.Firefox()
url='https://www.amazon.com/gp/gw/ajax/s.html'
driver.get(url)

driver.get_screenshot_as_file('image.jpg')

