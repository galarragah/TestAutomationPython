from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('Hola Prro')
driver.find_element_by_name('submit_search').click()
tc.assertEqual('No results were found for your search "Hola Prro"',driver.find_element_by_xpath('//*[@id="center_column"]/p'))
time.sleep(2)
driver.find_element_by_link_text('Women').click()
time.sleep(2)
driver.find_element_by_partial_link_text('Dress').click()
time.sleep(2)
driver.find_element_by_link_text('Casual Dresses').click()
driver.close
driver.quit()
