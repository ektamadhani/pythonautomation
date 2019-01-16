from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.firefox()
driver.get("https://demo.actitime.com")
try:
    element=webdriver(driver,10).until
