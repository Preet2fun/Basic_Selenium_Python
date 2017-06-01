import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GoogleOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()


    def test_switch_window(self):
        #This will throw a TimeoutException whenever the page load takes more than 30 seconds. But this will only effects to get URL line only. In code if any another
        #page is going to open then we have to define page timeout again for that page or URL of that page.
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.driver.get("http://uanmembers.epfoservices.in/")
        window_before = self.driver.window_handles[0]
        time.sleep(5)
        print (window_before)

        self.driver.find_element_by_link_text('Know your UAN Status').click()
        after_handler = self.driver.window_handles[1]
        time.sleep(5)
        print (after_handler)
        self.driver.switch_to_window(after_handler)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
