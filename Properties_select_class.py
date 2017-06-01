from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class Properties_Select(unittest.TestCase):

    def setUp(self):
        # Create New Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_Properties_select_class(self):

        # Navigate to URL
        self.driver.get("https://www.amazon.in/")
        select = Select(self.driver.find_element_by_id("searchDropdownBox"))

        print("------------Display first element from dropdown--------------------------")
        elem = select.first_selected_option
        print(elem.text)
        elem1 = select.select_by_visible_text('Amazon Fashion')


        print("------------Display all selected from dropdown--------------------------")
        temp = list()
        temp = select.all_selected_options
        for a in temp:
            assert isinstance(a.text, object)
        print(a.text)

        print("------------Display all available options from dropdown--------------------------")
        temp1 = list()
        temp1 = select.options
        i = len(temp1)
        print (i)

        print (temp1[2].text)

        for a in temp1:
            assert isinstance(a.text, object)
            print(a.text)



    def tearDown(self):
        # close the firefox session
        self.driver.quit()
        #self.driver.close()


if __name__=='__main__':
    unittest.main(verbosity=2)