from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obl=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obl)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window

print(driver.title)
print(driver.current_url)
print(driver.page_source)
time.sleep(5)
