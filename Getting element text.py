from selenium import webdriver

driver = webdriver.Firefox()
url='http://www.bbc.com/sport/0/'
driver.get(url)

x = driver.find_element_by_class_name('primary-nav__items')
y = x.text

print '========================================'
print y
print '========================================='