import unittest
from time import sleep

from common.selenium_driver import selenium_driver


class MyUnit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #获取驱动对象
        self.driver = selenium_driver()



    @classmethod
    def tearDownClass(self):
        sleep(2)
        self.driver.quit()

