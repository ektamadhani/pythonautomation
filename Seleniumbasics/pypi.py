from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://pypi.org/")
driver.find_element(By.CSS_SELECTOR,'[class="homepage-banner"]').click()
driver.find_element_by_css_selector(".homepage-banner").click()
driver.find_element_by_css_selector('[class^="homepage"]').click()
driver.find_element_by_css_selector('[class$="banner"]').click()
driver.find_element_by_css_selector('[class*="home"]').click()
driver.find_element_by_css_selector('[id="search"]').click()
driver.find_element_by_css_selector("#search").click()
driver.find_element_by_css_selector('[id^="se"]').click()
driver.find_element_by_css_selector('[id$="ch"]').click()
driver.find_element_by_css_selector('[iD*="ea"]').click()
driver.find_element_by_css_selector('[name="q"]').click()
driver.find_element_by_css_selector('[name^="q"]').click()
# driver.find_element_by_css_selector('[name$="q"]').click()
# driver.find_element_by_css_selector('[name*="m"]').click()



driver.find_element_by_xpath("//input[contains(id,search)]").click()
driver.find_element_by_xpath('//h2[text()="Trending projects"]').click()