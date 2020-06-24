from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import time
import unittest

driver = webdriver.Chrome("../chromedriver.exe")

class UnitTest(unittest.TestCase):

    def setUp(self):
        configuracion = configparser.ConfigParser() 
        configuracion.read('configuracion.ini') #READ SIRVE PARA LEER ARCHIVOS
        configuracion.sections()
        obtener_explorador = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['page']
        self.driver = webdriver.Chrome(obtener_explorador)

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.page)
        myDynamicElement = driver.find_element_by_name("q")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
