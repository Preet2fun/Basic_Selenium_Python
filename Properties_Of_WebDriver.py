from selenium import webdriver
import unittest


class Search_function(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        # Create New Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # Navigate to URL
        cls.driver.get("https://www.amazon.in/")

    def test_properties_webdriver_class(self):
        # Get the title of page
        self.elem = self.driver.title
        print(self.elem)
        # check for received title is correct or not using assertion method
        self.assertEqual(self.elem,"Online Shopping: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        #This gets the URL of the current page displayed in the browser
        print(self.driver.current_url)
        #This gets the handle of the current window
        print(self.driver.current_window_handle)
        # This gets the name of the underlying browser for this instance
        print(self.driver.name)
        # This gets the current orientation of the device
        #print(self.driver.orientation)
        # This gets the source of the current page
        #print(self.driver.page_source)
        # This gets the handles of all windows within the current session
        print(self.driver.window_handles)

    def test_methods_webdriver_class(self):

        #this goes one step backward in the browser history in the current session.
        self.driver.find_element_by_id("nav-logo").click()
        self.driver.implicitly_wait(30)
        self.driver.back()
        self.driver.implicitly_wait(30)
        # This goes one step forward in the browser history in the current session.
        self.driver.forward()
        self.driver.implicitly_wait(30)
        #This refreshes the current page displayed in the browser.
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        # This returns the element with focus or the body if nothing else has focus.
        self.driver.switch_to_active_element()

    @classmethod
    def tearDownClass(cls):
        # close the firefox session
        cls.driver.quit()



if __name__=='__main__':
    unittest.main(verbosity=2)