from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_test(self):
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')
        time.sleep(3)
        driver.find_element_by_link_text('Women').click()
        time.sleep(4)
        driver.find_element_by_id('search_query_top').send_keys("Ropa", Keys.ENTER)
        time.sleep(4)
        driver.get('http://google.com')
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.execute_script("window.open()")   
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        
        
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
