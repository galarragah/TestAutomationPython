from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.w3schools.com/html/default.asp")
driver.get_screenshot_as_file("C:\\Users\\hgalarraga\\Desktop\\ProyectoAutomation\\PruebaImagenII.png")
driver.close()
driver.quit()
