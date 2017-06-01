from castro import Castro
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import datetime

class DragAndDropTest (unittest.TestCase):
    URL = "http://jqueryui.com/resources/demos/droppable/default.html"

    def setUp(self):
        #self.screenCapture = Castro(Castro(filename="testSearchByCategory.swf"))
        c = Castro(filename="testSearchByCategory.swf")
        c.start()
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        c.stop()

    def test_drag_and_drop(self):
        driver = self.driver
        source = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("droppable")
        time.sleep(5)
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        file_name = st + ".png"
        driver.save_screenshot(file_name)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        time.sleep(5)
        file_name1 = st + ".png"
        driver.save_screenshot(file_name1)
        print(target.text)

        #try:
            #temp = driver.find_element_by_id("abc")
            #self.assertEquals('Droppeda!',temp.text)
        #except NoSuchElementException:
            #raise

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)