from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys




class Unittest(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome('chromedriver.exe')


    def test_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_elements_by_tag_name("option")
        time.sleep(3)
        for option in opcion:
            print("Los valores son %s " % option.get_attribute("value"))
            option.click()
            time.sleep(1)
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
        