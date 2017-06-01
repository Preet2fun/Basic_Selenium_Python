import unittest
from xmlrunner import xmlrunner
from google_home import HomePageTest
from class_level_setup_teardown import Search_function


# get all tests from HomePageTest and Search_function class
search_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
Home_page_tests = unittest.TestLoader().loadTestsFromTestCase(Search_function)


# create a test suite combining search_test and home_page_test
smoke_test = unittest.TestSuite([search_tests,Home_page_tests])


# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_test)
#unittest.TextTestRunner(verbosity=2).run(smoke_test)

