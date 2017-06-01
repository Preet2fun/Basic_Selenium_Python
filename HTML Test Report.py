import unittest
import HTMLTestRunner
from HTMLTestRunner import *
import os
from google_home import HomePageTest
from class_level_setup_teardown import Search_function

#get the directory path to output report file
dir = os.getcwd()

# get all tests from HomePageTest and Search_function class
search_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
Home_page_tests = unittest.TestLoader().loadTestsFromTestCase(Search_function)

# create a test suite combining search_test and home_page_test
smoke_test = unittest.TestSuite([search_tests,Home_page_tests])

# open the report file
outfile = open(dir + "\Smoke_Test_Report.html","w")

# configure HTMLTestRunner options

runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Smoke Tests')
# run the suite using HTMLTestRunner
runner.run(smoke_test)

