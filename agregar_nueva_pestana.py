from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

class suite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_ventanas(self):
        driver = self.driver
        driver.get("https://www.google.com/intl/es/gmail/about/#")
        time.sleep(2)
        siguiente = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]")
        siguiente.click()
        print(driver.current_window_handle)
        time.sleep(3)

        handles = driver.window_handles
        for handles in handles:
            driver.switch_to.window(handles)
            time.sleep(3)
            print(driver.title)
        

    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()