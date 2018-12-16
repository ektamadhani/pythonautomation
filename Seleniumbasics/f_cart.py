from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.get_window_size()
driver.back()
driver.forward()
