from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import unittest
import time

class Alert_Types(unittest.TestCase):

    def setUp(self):
        # Create New Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_Alert_Types_class(self):

        # Navigate to URL

        self.driver.get("http://192.168.2.20:1601/public/main")
        elem = self.driver.find_element_by_id("txtUserName")
        elem.send_keys('admin')

        elem = self.driver.find_element_by_id("txtPassword")
        elem.send_keys('brijesh84')

        elem = self.driver.find_element_by_id("sbtnLogin").click()

        time.sleep(5)
        elem = self.driver.find_element_by_css_selector("body > header > div > div.menu_nav.primary > ul > li.tools > a > div.menu_name").click()

        time.sleep(5)
        elem = self.driver.find_element_by_id("Row9_Col0").click()
        elem = self.driver.find_element_by_css_selector("#sbtEmailaccountDelete > div.button_text").click()

        #Switch to alert
        alert = self.driver.switch_to_alert()

        #Print alert text
        alert_text = alert.text
        print(alert_text)

        # check alert text
        #self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)

        # click on Ok button
        #alert.accept()

        # click on cancel button
        #alert.dismiss()

    def tearDown(self):
        # close the firefox session
        self.driver.quit()
        #self.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)