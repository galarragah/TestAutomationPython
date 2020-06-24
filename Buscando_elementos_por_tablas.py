from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(4)


valor = driver.find_element_by_xpath('//*[@id="customers"]/tbody/tr[1]').text

print(valor)

rows=len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr'))
col = len(driver.find_elements_by_xpath('//*[@id="customers"]/tbody/tr[1]/th'))

print(rows)
print(col)

print(valor)
for n in range(2, rows+1):
    for b in range(1, col+1):
        dato = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
        print(dato, end='                               ')
    print()
  

driver.close()
driver.quit()