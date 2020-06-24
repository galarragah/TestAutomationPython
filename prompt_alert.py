from selenium import webdriver
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get("file:///C:/Users/hgalarraga/Desktop/ProyectoAutomation/ALERT/prompt_alert.html")
time.sleep(2)

prompt_alert = driver.find_element_by_name("prompt_alert").click()
time.sleep(1)

prompt_alert = driver.switch_to.alert
prompt_alert.accept()
time.sleep(4)

driver.close()
driver.quit()