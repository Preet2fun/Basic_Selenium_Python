from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('https://www.google.com/')
elem = driver.find_element('id','lst-ib')
elem.send_keys('pratik patel university of bridgeport')
elem.send_keys(Keys.ENTER)

