from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
listofimg = driver.find_elements_by_xpath("//img")
for i in listofimg:
    images=i.get_attribute("src")
    print(len(images))
