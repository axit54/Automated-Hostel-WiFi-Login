from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://192.168.10.3/connect/PortalMain')  
time.sleep(6)
username = browser.find_element_by_id("LoginUserPassword_auth_username")  
username.send_keys("your_reg_no")  

password = browser.find_element_by_id("LoginUserPassword_auth_password") 
password.send_keys("your_password")

browser.find_element_by_id("UserCheck_Login_Button").click()

