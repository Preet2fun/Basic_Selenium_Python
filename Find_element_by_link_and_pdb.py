
from selenium import webdriver
import pdb

driver = webdriver.Firefox()
driver.get('http://www.google.com')

pdb.set_trace()

x=driver.find_element_by_link_text('Gmail')
x.click()

pdb.set_trace()

y=driver.find_element_by_partial_link_text('Need')
y.click()

