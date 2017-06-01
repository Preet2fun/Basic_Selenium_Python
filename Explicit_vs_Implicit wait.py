
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(30)
url='http://www.google.com'
driver.get(url)

x=driver.find_element_by_link_text('Gmail')
x.click()

y=WebDriverWait(driver,20).until(EC.presence_of_element_located(('id','link-forgot-passwd')))
print ('Well Done Pratik !!!! You have done it')
