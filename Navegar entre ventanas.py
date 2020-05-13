from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys

class UniTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_navegacion_entre_ventanas(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

