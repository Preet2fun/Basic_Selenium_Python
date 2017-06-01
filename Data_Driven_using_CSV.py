import csv
import unittest
from selenium import webdriver

def getNumberofCount(filename):
    with open(filename,newline='') as f:
                reader=csv.reader(f)
                next(reader, None)  # skip the headers
                row_count = sum(1 for row in reader)
                return row_count

class SerachCsvDDT(unittest.TestCase):

    def setUp(self):
            self.driver=webdriver.Firefox()

    def test_CSV_read(self):
        No_of_rows=getNumberofCount('testdata.csv')
        print('No of Rows :',No_of_rows)
        driver=self.driver
        with open('testdata.csv',newline='') as testdatafile:
            driver=self.driver
            self.driver.get('http://www.google.com')
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            reader=csv.reader(testdatafile)
            next(reader, None)
            for row in reader:
                print(row[0],',',row[1])
                elem = self.driver.find_element_by_name("q")
                elem.send_keys(row[0])
                elem.submit()
                print(self.driver.title)
                self.assertTrue(self.driver.title,row[1])

    def tearDown(self):
                self.driver.close()

if __name__=="__main__":
    unittest.main()


