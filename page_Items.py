from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems:
    def __init__(self, my_driver):
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.driver = my_driver
        self.order = (By.ID, 'selectProductSort')

    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner).text

    def select_by_text(self, texto):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(texto)
        
    def select_by_value(self, value):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_value(value)

    def select_by_index(self, index):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_index(index)
        
    

    