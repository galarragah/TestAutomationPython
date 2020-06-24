from selenium import webdriver
import unittest
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get("file:///C:/Users/hgalarraga/Desktop/ProyectoAutomation/ALERT/alert_simple.html")
time.sleep(2)

alerta_simple = driver.find_element_by_name("alert").click()
time.sleep(2)

alerta_simple=driver.switch_to.alert.dismiss()
#alerta_simple.dismiss()
time.sleep(2)


driver.close()
driver.quit()
