from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(2)

all_cookies = driver.get_cookies()

print(all_cookies)

driver.close()
driver.quit()