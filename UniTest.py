from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys #Enviar acciones de teclado
import time


class Unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_buscar(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elemento = driver.find_element_by_name("q")
        elemento.send_keys("Selenium")
        elemento.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No se encontro el elemento: " not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

    
