import sys
import unittest
from selenium import webdriver


class SearchProducts(unittest.TestCase):
    PLATFORM = 'Mac OS X 10.9'
    BROWSER = 'chrome'
    SAUCE_USERNAME = 'preet2fun'
    SUACE_KEY = 'e52ac825-f8a1-4f63-81f7-fbed1b2b7b10'

    def setUp(self):
        print("Lets start")

    def test_start(self):
        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER
        #If you wanted to run on Sauce, you would instead use webdriver.Remote(),
        # and then pass it two paramaters: command_executor, which points to the Sauce cloud and
        # uses your Sauce Labs authentication to log in, and desired_capabilties, which specifies the browsers and operating
        # systems to run the tests against.

        sauce_string = self.SAUCE_USERNAME + ':' + self.SUACE_KEY
        self.driver = webdriver.Remote('http://' + sauce_string +'@ondemand.saucelabs.com:80/wd/hub', desired_caps)
        self.driver.get('https://www.google.co.in')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    # below code is use for passing arrgument when we run code using command line. It will accept two argument, one is browser and another is OS
    if len(sys.argv) > 1:
        SearchProducts.BROWSER = sys.argv.pop()
        SearchProducts.PLATFORM = sys.argv.pop()
    unittest.main(verbosity=2).driver.maximize_window()