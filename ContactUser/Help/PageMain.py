from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Help.Log import Logs

class PageMain:
    def __init__(self, driver):
        self.driver = driver
        self.click_contact_us = (By.XPATH, '//a[@title="Contact Us"]')
        self.select_subject = (By.XPATH, '//select[@id="id_contact"]')
        self.email = (By.XPATH, '//input[@id="email"]')
        self.order_reference = (By.XPATH, '//input[@id="id_order"]')
        self.file_upload = (By.XPATH, '//input[@id="fileUpload"]')
        self.message = (By.XPATH, '//textarea[@id="message"]')
        self.send = (By.XPATH, '//span[contains(text(),"Send")]')
        self.log = Logs()

    def click_contact(self):
        self.driver.find_element(*self.click_contact_us).click()
        self.log.log("INFO", " SE HIZO CLIC")

    def select_subject_heading(self, opcion):
        order = Select(self.driver.find_element(*self.select_subject))
        order.select_by_visible_text(opcion)
        self.log.log("INFO", " Digito "+opcion)

    def type_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)
        self.log.log("INFO", " Digito " + email)

    def type_order_reference(self, reference):
        self.driver.find_element(*self.order_reference).send_keys(reference)
        self.log.log("INFO", " Referencia" + reference)

    def uploand_file(self, ruta):
        self.driver.find_element(*self.file_upload).send_keys(ruta)
        self.log.log("INFO", " Ruta de imagen " + ruta)

    def type_message(self, text):
        self.driver.find_element(*self.message).send_keys(text)
        self.log.log("INFO", " Texto " + text)

    def enter_send(self):
        self.driver.find_element(*self.send).click()
        self.log.log("INFO", " SE ENVIO EL FORMULARIO")