from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver=webdriver.Chrome()
driver.get("https://timetracker.ctepl.com/actitime/login.do")
time.sleep(3)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("pwd")
# driver.find_element(By.CSS_SELECTOR,"[id='username]").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR,"[name='pwd']").send_keys("manager")
driver.find_element(By.CSS_SELECTOR,"[id='loginButton']").click()
print("logged in")