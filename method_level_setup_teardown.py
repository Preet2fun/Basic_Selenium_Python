from selenium import webdriver
import unittest


class Search_function(unittest.TestCase):

    def setUp(self):
        # Create New Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # Navigate to URL
        self.driver.get("https://www.amazon.in/")

    def test_get_the_title(self):
        # Get the title of page
        self.elem = self.driver.title
        print(self.elem)
        # check for received title is correct or not using assertion method
        self.assertEqual(self.elem,"Online Shopping: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")

    def test_search_by_name(self):
        # get the search box and clear if any content is there in it
        self.search_field = self.driver.find_element_by_id("twotabsearchtextbox")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

    def tearDown(self):
        # close the firefox session
        self.driver.quit()



if __name__=='__main__':
    unittest.main(verbosity=2)