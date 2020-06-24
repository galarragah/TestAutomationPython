class Elementos:

    def __init__(self, import_driver):
        self.search_query_top = 'search_query_top'
        self.submit_search = 'submit_search'
        self.color_naranja = 'color_1'
        self.cantidad = 'qty'
        self.aumentar_cantidad = "//*[@id='quantity_wanted_p']/a[2]/span/i"
        self.driver = import_driver

    def search(self, texto):
        self.driver.find_element_by_id(self.search_query_top).send_keys(texto)
        self.driver.find_element_by_name(self.submit_search).click()

    def selection_color(self):
        self.driver.find_element_by_id(self.color_naranja).click()

    def digitar_cantidad(self, numero):
        self.driver.find_element_by_name(self.cantidad).clear()
        self.driver.find_element_by_name(self.cantidad).send_keys(numero)

    def aumentar_contador(self):
        for n in range(3):
            self.driver.find_element_by_xpath(self.aumentar_cantidad).click()

    def verificar_cantidad(self):
        return self.driver.find_element_by_name(self.cantidad).get_attribute('value')

