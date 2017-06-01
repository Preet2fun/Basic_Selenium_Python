import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class SerachDDT(unittest.TestCase):

    def setUp(self):
        print ("Lets start")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")
    @data(("phones","Phones - Google Search"),("music","music - Google Search"))
    @unpack


    def test_Google_Search_FF(self, search_value, Expected_result):
        driver = self.driver
        driver.get("http://www.google.com")
        input_element = driver.find_element_by_name("q")
        print(search_value)
        input_element.send_keys(search_value)
        input_element.submit()
        self.assertEqual(driver.title, Expected_result)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
