from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")

driver=webdriver.Chrome(service=ser_obj,options=ops)

driver.get("https://whatmylocation.com/")

