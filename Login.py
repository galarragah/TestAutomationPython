from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://usfla0294/MSID_441_DEV/xsm441/xsm/Login#")


time.sleep(4)

driver.find_element_by_xpath("//*[@id='login']/form/div[2]/div/div/input").click()


time.sleep(5)


usuario = driver.find_element_by_id("username")
usuario.send_keys("xs2")
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("xs2")
clave.send_keys(Keys.ENTER)
time.sleep(3)

driver.close()