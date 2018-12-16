from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
listofimg = driver.find_element_by_xpath("//img")
#print("len(listofimg)")
for i in listofimg:

