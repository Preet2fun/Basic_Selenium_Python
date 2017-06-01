
from selenium import webdriver

driver = webdriver.Firefox()
url='http://www.echoecho.com/htmlforms09.htm'
driver.get(url)

def checkbox(element):
    element_type = element.get_attribute('type')

    if element_type != 'checkbox':
        raise AssertionError('The passed element is not a check box')

def checkbox_selected(element):
    checkbox(element)

    if element.is_selected():
        return True
    else:
        print 'Sorry ! you got wrong one'

my_checkbox = driver.find_element_by_name('option2')
#x = my_checkbox.find_element_by_name('option1')
print checkbox_selected(my_checkbox)

