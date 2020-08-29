from selenium.webdriver.common.by import By

class MessageVerified:
    def __init__(self, driver):
        self.driver = driver
        self.message_text = (By.XPATH, '//p[@class="alert alert-success"]')


    def text_message(self):
        return self.driver.find_element(*self.message_text).text
