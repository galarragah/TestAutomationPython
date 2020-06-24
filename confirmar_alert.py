from selenium import webdriver
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get("file:///C:/Users/hgalarraga/Desktop/ProyectoAutomation/ALERT/confirmar_alert.html")
time.sleep(2)

confirm_alert = driver.find_element_by_name("confirmar_alert").click()
time.sleep(2)
confirm_alert = driver.switch_to.alert
confirm_alert.accept()
confirm_alert.dismiss()
time.sleep(2)
driver.close()
driver.quit()

