from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
#from __builtin__ import classmethod


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        #cls.driver.get("https://www.google.co.in")

    def test_home_page(self):
        #self.assertTrue(self.driver.find_element(By.ID,"lst-ib"))
        #print("Element is present")
        print("Pratik")

    @classmethod
    def tearDown(cls):
        cls.driver.close()
