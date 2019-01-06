from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Ekta/Desktop/pratice.html")
time.sleep(5)
value1 = driver.find_element_by_xpath('//*[@id="Pythonradio"]').is_displayed()
print(value1)
value2 = driver.find_element_by_xpath('//*[@id="Pythonradio"]').is_enabled()
print(value2)
value3 = driver.find_element_by_xpath('//*[@id="Pythonradio"]').is_selected()
print(value3)
driver.find_element_by_xpath('//*[@id="Pythonradio"]').click()
value4 = driver.find_element_by_xpath('//*[@id="Pythonradio"]').click()
print(value4)


