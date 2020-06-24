from selenium import webdriver

import time
import unittest
from PaginaElementos import Elementos

class BuscarAgregarCamisetas(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get("http://automationpractice.com/index.php")
        self.paginaElementos = Elementos(self.driver)
        #self.driver.find_element_by_

    def test_search_find_tshirt(self):
        self.paginaElementos.search('T-shirts')
        time.sleep(2)
        self.paginaElementos.selection_color()
        time.sleep(2)
        self.paginaElementos.digitar_cantidad(25)
        time.sleep(2)
        self.paginaElementos.aumentar_contador()
        time.sleep(2)    
        self.assertEqual(self.paginaElementos.verificar_cantidad(), '28',)
        time.sleep(3)

    
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()