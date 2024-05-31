from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()

# ser_obj=Service("C:\Ddrivers\chromedriver\chromedriver_win32.exe")
# driver=webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/")
driver.get("http://www.automationpractice.pl/index.php")

driver.back()
driver.forward()
driver.refresh()

driver.quit()