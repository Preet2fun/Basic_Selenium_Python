import unittest
import HTMLTestRunner
from HTMLTestRunner import *
import os
from google_home import HomePageTest
from class_level_setup_teardown import Search_function



if __name__ == "__main__":
  #testSuite = unittest.TestSuite(suites)
  search_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
  Home_page_tests = unittest.TestLoader().loadTestsFromTestCase(Search_function)
  smoke_test = unittest.TestSuite([search_tests,Home_page_tests])
  runner = unittest.TextTestRunner(verbosity=1)
  filename = "Test1.html"
  output = open (filename,"wb")
  runner = HTMLTestRunner.HTMLTestRunner(
         stream=output,
         title="Test report"
     )
  runner.run(smoke_test)
if __name__=="__main__":
    HTMLTestRunner.main()