from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundos
        driver.get("https://www.google.com")
        myDynamicElement = driver.find_element_by_name("q")

    def teardown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()


