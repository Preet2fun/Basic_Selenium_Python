from selenium import webdriver
import logging
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import os

class DragAndDropTest (unittest.TestCase):
    URL = "http://jqueryui.com/resources/demos/droppable/default.html"
    logging.basicConfig(filename="log_file.txt", level=logging.DEBUG)
    #print(os.sep)
    #logfile = 'logs' + os.sep + ((__file__.upper())[(__file__.rfind(os.sep)+1):]).replace('.PY', '.log')
    #logging.basicConfig(format= '%(asctime)-12s [%(filename)-10s] %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S', filename=logfile, filemode='w', level=logging.INFO)

    def setUp(self):
        self.driver = webdriver.Firefox()
        logging.debug('URL Get Open')
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_drag_and_drop(self):
        driver = self.driver
        source = driver.find_element_by_id("draggable")
        logging.debug('Source Target Found')
        target = driver.find_element_by_id("droppable")
        logging.debug('Destination Target Found')
        time.sleep(5)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        print(target.text)
        self.assertEquals('Dropped!',target.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)