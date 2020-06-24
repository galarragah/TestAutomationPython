from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://usfla0764/DINANTHN/xsm/Login")


time.sleep(3)



driver.find_element_by_class_name("select-wrapper").click()

driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/form/div[2]/div/div/ul/li[2]/span").click()


time.sleep(3)
usuario = driver.find_element_by_id("username")
usuario.send_keys("xs2")
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("xs2")
clave.send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element_by_class_name("collapsible-header").click()

time.sleep(5)

driver.find_elements_by_class_name("collection-item")[1].click()
time.sleep(10)

driver.close()