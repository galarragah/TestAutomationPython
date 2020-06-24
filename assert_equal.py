from selenium import webdriver
import unittest
import time

class suite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_assert_equal(self):
        self.driver.get("https://www.google.com/")
        titulo_pagina = self.driver.title
        self.assertEqual(titulo_pagina, 'Google')

    def test_assert_no_equal(self):
        self.driver.get("https://www.google.com/")
        titulo_pagina = self.driver.title
        self.assertNotEqual(titulo_pagina, 'Google')
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()