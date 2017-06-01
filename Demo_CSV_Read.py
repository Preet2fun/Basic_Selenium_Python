import csv
import unittest
from selenium import webdriver

##define a function that returns number of rows in a csv file

def getNumberOfCount(filename):
        with open(filename,newline='') as f:
                reader=csv.reader(f)
                next(reader, None)  # skip the headers
                row_count = sum(1 for row in reader)
                return row_count

class SiteInfoVerification(unittest.TestCase):

##setup method

        def setUp(self):
                self.driver=webdriver.Firefox()
##test method

        def test_site_info_verification(self):
                numberOfSites=getNumberOfCount('siteinfo.csv')
                print("Number of Sites: ",numberOfSites)
                driver = self.driver
                with open('siteinfo.csv',newline='') as SiteInfoFile:
                        driver=self.driver
                        reader=csv.reader(SiteInfoFile)
                        next(reader, None)  # skip the headers
                        for row in reader:
                                print(row[0],",",row[1])
                                driver.get(''.join(row[0]))
                                self.assertIn(''.join(row[1]),driver.title)

##tear down method

        def tearDown(self):
                self.driver.close()



if __name__=="__main__":
        unittest.main()