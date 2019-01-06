from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Ekta/Desktop/pratice.html")
driver.find_element(By.ID,"Pythonradio").click()
driver.find_element(By.NAME,"Course").click()
# driver.find_element(By.CSS_SELECTOR,"id=Pythonradio").click()
# driver.find_element(By.CSS_SELECTOR,"name=Course").click()
time.sleep(3)
driver.find_element(By.ID,"Seleniumradio").click()
#cerwdriver.find_element(By.NAME,"Course").click()

# driver.find_element(By.CSS_SELECTOR,"id=Seleniumradio").click()
# driver.find_element(By.CSS_SELECTOR,"name=Course").click()
print("finished")

