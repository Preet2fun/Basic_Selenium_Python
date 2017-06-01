from selenium import webdriver

driver = webdriver.Firefox()
url='http://pioneerdemo.com/pioneersitenew/contact/'
driver.get(url)

x=driver.find_element_by_class_name('wpcf7')
y=driver.find_element_by_tag_name('textarea')

z=y.get_attribute('value')
print z

a=y.get_attribute('cols')
print a

b=y.get_attribute('rows')
print b


