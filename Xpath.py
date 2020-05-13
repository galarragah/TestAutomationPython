from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class Unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_buscar_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(3)
        buscar_xpath = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        time.sleep (3)
        buscar_xpath.send_keys("SELENIUM", Keys.ARROW_DOWN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()