from selenium import webdriver
import unittest
import time
from pageIndex import PageIndex
from page_Items import PageItems
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):


    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        #option.add_argument("incognito")
        option.add_argument("--headless") #NO SE LEVANTA EL BROWSER
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(5)
        #self.driver.set_window_position(150, 200)
        #self.driver.maximize_window() #Ventana completa
        #self.driver.set_window_size(200, 240)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)

    @unittest.skip("Negativo")
    def test_search_no_elements(self):
        self.indexPage.search('Hola')
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "Hola"')
        
        
        
    @unittest.skip("Not needed now")
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())
        
        
    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_by_text('Product Name: A to Z')
        time.sleep(4)
        self.itemsPage.select_by_value('reference:asc')
        #self.driver.save_screenshot('Lista.png') #TOMAR FOTO
        time.sleep(3)
        self.itemsPage.select_by_index(3)
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
