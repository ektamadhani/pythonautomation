from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
sourceCode = driver.page_source
print("sourceCode ")
