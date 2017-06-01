from selenium import webdriver
import unittest
import math


class assertion_practice(unittest.TestCase):

    def test_assertion(self):
        self.assertEquals(2,2,msg='Both values are same') # its true, that's why msg will not get display and interpreter execute next line
        print("successfully executed assertequals condition")

        self.assertEquals(2,3,msg='Both values are not same') #condition is false thats why AssertionError will get raise and execution will get stop
        print("AsserionError will get display with msg string")

        self.assertNotEqual(2,3,msg='Both values are not equal')# its true, that's why msg will not get display and interpreter execute next line
        print("successfully executed assertequals condition")

        self.assertNotEqual(2,2,msg='Both values are same...')#condition is false thats why AssertionError will get raise and execution will get stop
        print("AsserionError will get display with msg string")
