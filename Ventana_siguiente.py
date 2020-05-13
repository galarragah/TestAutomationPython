from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys

class Unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
    
    def test_pagina_siguiente(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        time.sleep(3)
        driver.get("http://google.com")
        time.sleep(3)
        driver.get("http://youtube.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.forward()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
     unittest.main()
