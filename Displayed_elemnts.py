from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys


class Unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_displayed_elements(self):
        driver=self.driver
        driver.get("https://google.com")
        time.sleep(5)
        #displae = driver.find_element_by_name("btnI")
        displae = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[2]")
        print(displae.is_displayed()) #Regresa true o false si ya cargo el elemento
        print(displae.is_enabled()) #Regresa un true o false si el elemento esta disponible
        


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()