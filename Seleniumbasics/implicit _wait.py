from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Verify_login:
    def Login(self):
        Driver=webdriver.Chrome()
        Driver.get("https://timetracker.ctepl.com/actitime/login.do")
        print("used implicit wait")
        Driver.maximize_window()
        Driver.find_element_by_id("username").clear()
        Driver.find_element_by_id("username").send_keys('admin')
        Driver.find_element_by_name("pwd").clear()
        Driver.find_element_by_name("pwd").send_keys("manager")
        Driver.find_element_by_xpath("//a[@id='login Button']")
        time.sleep(5)
        print("Login Succesfully")
Login_test=Verify_login()
Login_test.Login()






