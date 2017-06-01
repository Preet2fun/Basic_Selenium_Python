from behave import *
from selenium import webdriver

@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.get("https://www.amazon.in/")


@when('I search for {text}')
def step_i_search_for(context, text):
    search_field = context.driver.find_element_by_name("q")
    search_field.clear()
    # enter search keyword and submit
    search_field.send_keys(text)
    search_field.submit()

@then('I should see list of matching products in search results')
def step_i_should_see_list(context):
    print("Hello")

    