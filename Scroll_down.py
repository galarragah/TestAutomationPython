from selenium import webdriver
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.amazon.com/")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)

driver.close()
driver.quit()