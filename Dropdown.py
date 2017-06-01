from selenium import webdriver

driver = webdriver.Firefox()
url='https://www.amazon.com/gp/gw/ajax/s.html'
driver.get(url)

def dropdown(element):
    if element.get_attribute('type') not in ['select-one','select-multi']:
        raise AssertionError('The element is not in dropdown')
    return

def select_dropdown(element,text):
    dropdown(element)

    all_options = element.find_elements_by_tag_name('option')
    tmp = False
    for option in all_options:
        var = option.text

        if var==text:
            option.click()
            tmp = True
            break
    if not tmp:
        raise Exception('The requested options is not found in dropbox')
    return

my_dropdown = driver.find_element_by_class_name('nav-search-dropdown')
select_dropdown(my_dropdown,'Baby')
