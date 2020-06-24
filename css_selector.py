from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.w3schools.com/html')
time.sleep(4)

content = driver.find_element_by_css_selector('a.w3-blue')
content.click()

