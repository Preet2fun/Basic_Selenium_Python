from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class DoubleclickTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://api.jquery.com/dblclick/")
        self.driver.maximize_window()

    def test_double_click(self):
        driver = self.driver
        frame =  driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frame)
        time.sleep(5)
        box = driver.find_element_by_tag_name("div")

        self.assertEquals('rgba(0, 0, 255, 1)',box.value_of_css_property("background-color"))
        #ActionChains(driver).move_to_element(driver.find_element_by_tag_name("span")).perform()
        #time.sleep(5)
        ActionChains(driver).double_click(box).perform()
        time.sleep(5)

        print(box.value_of_css_property("background-color"))
        self.assertEqual('rgba(255, 255, 0, 1)',box.value_of_css_property("background-color"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
