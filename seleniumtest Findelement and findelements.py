from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common. by import By
import time

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/")

# find_element - return singale webelement

element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element.send_keys("laptop")

# find_elements  -  return maltipale webelement

element=driver.find_elements(By.XPATH,"")

# Element not avilable than throw NosuchelementExpection

login_element=driver.find_elements(By.LINK_TEXT,"Log in")
login_element.click()


time.sleep(5)
