from selenium import webdriver
import unittest
import time

class Unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_link_text(self):
        driver = self.driver
        driver.get("http://www.w3schools.com/")
        time.sleep(3)
        encontrar_link = driver.find_element_by_link_text("Learn PHP")
        encontrar_link.click()

if __name__ == '__main__':
    unittest.main()