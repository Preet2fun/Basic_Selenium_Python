from selenium import webdriver
import time

driver = webdriver.Firefox()
url='https://www.google.com'
driver.get(url)

time.sleep(5)
driver.get_window_size()

time.sleep(5)
driver.set_window_size(width=200,height=500)

time.sleep(5)
driver.set_window_size(width=500,height=200)

time.sleep(5)
driver.maximize_window()

time.sleep(5)
position = driver.get_window_position()
print position