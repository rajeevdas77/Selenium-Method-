from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(5)
driver.save_screenshot("C:\Users\MrDas\Documents\My Pictures\screenshot.png")