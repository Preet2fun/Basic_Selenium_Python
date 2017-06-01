from selenium import webdriver
import unittest


class Properties_WebElement(unittest.TestCase):

    def setUp(self):
        # Create New Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_Properties_webElement_class(self):

        # Navigate to URL
        self.driver.get("https://www.google.co.in")
        elem = self.driver.find_element_by_id("lst-ib")
        print ("------------------ Height---------------")
        print(elem.size)
        print ("-------------------Tag Name-------------")
        print(elem.tag_name)
        print ("-------------------Test-----------------")
        print (elem.text)

    def test_Methods_webElement_class(self):

        # Navigate to URL
        self.driver.get("https://www.google.co.in")
        elem = self.driver.find_element_by_id("lst-ib")
        print ("------------------ Attribute---------------")
        print(elem.get_attribute("value"))
        print(elem.get_attribute("maxlength"))
        self.assertEquals(elem.get_attribute("maxlength"),"2048")
    

        print ("------------------ element is displayed or not---------------")
        assert (elem.is_displayed())
        print("element is displayed")

        print ("------------------ element is enabled or not---------------")
        assert (elem.is_enabled())
        print("element is enabled")

        self.assertTrue(elem.is_displayed() and elem.is_enabled())
        print ("element is displayed and enabled")

        #print ("------------------ element is selected or not---------------")
        #assert (elem.is_selected())
        #print("element is selected")

        print ("------------------ CSS Properties of element---------------")
        print(elem.value_of_css_property("background-color"))
        print(elem.value_of_css_property("zIndex"))
        print(elem.value_of_css_property("border"))
        print(elem.value_of_css_property("padding"))

    def tearDown(self):
        # close the firefox session
        self.driver.quit()
        #self.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)