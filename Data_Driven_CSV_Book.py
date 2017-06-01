import csv
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import re

def get_data(filename):
                rows = []
                #with open(filename,newline='') as f:
                f = open(filename, "rb")
                reader=csv.reader(f)
                next(reader,None)
                for row in reader:
                    rows.append(row)
                    print(row)
                    print(rows)
                    return  rows
                #reader=csv.reader(f)
                #next(reader, None)
                #for row in reader:
                    #rows.append(row)
                    #print(rows)
                    #return rows

@ddt
class SerachCsvDDT(unittest.TestCase):

    def setUp(self):
        print ("Lets start")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")

    @data(*get_data("testdata.csv"))
    @unpack


    def test_Google_Search_FF(self, search_value, Expected_result):
        driver = self.driver
        elem = self.driver.find_element_by_id("lst-ib")
        elem.send_keys(search_value)
        elem.submit()
        print(self.driver.title)
        self.assertEqual(self.driver.title, Expected_result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()