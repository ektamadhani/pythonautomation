from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.find_element_by_xpath("//*[@id='top']/nav/ul/li[4]/a").click()
