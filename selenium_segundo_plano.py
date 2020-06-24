from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

palabra_busqueda = "sele"
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
driver.get("https://www.google.com/")
time.sleep(3)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(3)

for i in range(1,11):
    elementos = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div/span/b").text
    print(palabra_busqueda + elementos)

driver.close()