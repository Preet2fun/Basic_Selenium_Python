
from selenium import webdriver

driver = webdriver.Firefox()
url='http://www.echoecho.com/htmlforms10.htm'
driver.get(url)

def Radio_Button(element):
    element_type = element.get_attribute('type')

    if element_type != 'radio':
        raise AssertionError('The passed element is not a radio button')

def Radio_Button__selected(element):
    Radio_Button(element)

    if element.is_selected():
        return True
    else:
        print 'Sorry ! you got wrong one'

def Select_Radio_Button(elements,value):

    for element in elements:
        Radio_Button(element)
        current_value = element.get_attribute('value')
        var = False

        if current_value == value:
            element.click()
            var = True
            break
    if not var:
        raise AssertionError('None of radio button have requseted value')

    return


my_radio = driver.find_elements_by_name('group1')
#x = my_checkbox.find_element_by_name('option1')
print my_radio
print type(my_radio)

Select_Radio_Button(my_radio,'Cheese')


