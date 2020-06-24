from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageIndex:
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search' )
        #self.query_top = 'search_query_top'
        #self.query_button = 'submit_search'
        self.driver = my_driver

    def search(self, texto):
        try:
            search_box = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.query_top))
            search_box.send_keys(texto)
            search_button = WebDriverWait(self.driver,4).until(EC.element_to_be_clickable(self.query_button))
            search_button.click()
        except:
            print('NO SE ENCUENTRA EL ELEMENTO')
        #self.driver.find_element(*self.query_top).send_keys(texto)
        #self.driver.find_element(*self.query_button).click()
        #self.driver.find_element_by_id(self.query_top).send_keys(texto)
        #self.driver.find_element_by_name(self.query_button).click()
