from selenium import webdriver
import time
import unittest
import HtmlTestRunner

class suite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_busqueda(self):
        self.driver.get("https://www.google.com/")
        self.busqueda = self.driver.find_element_by_name('q')
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(3)

    def test_scroll_down(self):
        self.driver.get("https://www.amazon.com/")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)

    def test_link_text(self):
        self.driver.get("http://www.w3schools.com/")
        time.sleep(3)
        encontrar_link = self.driver.find_element_by_link_text("Learn PHP")
        encontrar_link.click()

    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultados Test'))