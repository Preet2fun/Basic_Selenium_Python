from selenium import webdriver

driver = webdriver.Firefox()
url='http://www.google.com'
driver.get(url)

def find_and_assert_element_visible(locator_type,search_term):

    element = driver.find_element(locator_type,search_term)

    if not element.is_displayed():
        raise AssertionError('Element not visible')
    else:
        print 'Element is visible. ;)'

find_and_assert_element_visible('id','lga')
