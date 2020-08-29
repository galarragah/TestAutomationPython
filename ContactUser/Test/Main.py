from selenium import webdriver
import unittest
from Help.PageMain import PageMain
from Help.MessageVerified import MessageVerified
from Help.Log import Logs
import time

class Contact_User(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\\drivers\\chromedriver.exe')
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(10)
        self.page_main = PageMain(self.driver)
        self.page_message = MessageVerified(self.driver)
        self.log = Logs()

    def test_contact_user(self):
        self.log.log("INFO", True)
        self.page_main.click_contact()
        self.page_main.select_subject_heading("Webmaster")
        self.page_main.type_email("test@gmail.com")
        self.page_main.type_order_reference("Test Test Test")
        self.page_main.uploand_file("C:\\Users\\hgalarraga\\Desktop\\ProyectoAutomation\\Lista.png")
        self.page_main.type_message("PRUEBA MENSAJE TEST")
        self.page_main.enter_send()
        self.assertEqual(self.page_message.text_message(), 'Your message has been successfully sent to our team.')

        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()