import sys
import unittest
from selenium import webdriver


class SearchProducts(unittest.TestCase):
    PLATFORM = 'WINDOWS'
    BROWSER = 'firefox'
    #SAUCE_USERNAME = 'preet2fun'
    #SUACE_KEY = 'e52ac825-f8a1-4f63-81f7-fbed1b2b7b10'

    def setUp(self):
        print("Lets start")

    def test_start(self):
        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER
        # below mention IP is HUB ip, where hub is running.
        self.driver = webdriver.Remote('http://192.168.12.151:4444/wd/hub', desired_caps)
        #sauce_string = self.SAUCE_USERNAME + ':' + self.SUACE_KEY
        #self.driver = webdriver.Remote('http://' + sauce_string +'@ondemand.saucelabs.com:80/wd/hub', desired_caps)
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
