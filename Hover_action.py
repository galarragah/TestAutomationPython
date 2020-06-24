from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest


class Unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_hover_action(self):
        driver = self.driver
        driver.get("https://google.com")
        time.sleep(3)
        elemen = driver.find_element_by_link_text("Privacidad")

        hover = ActionChains(driver).move_to_element(elemen)
        hover.perform()
        time.sleep(3)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()