from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

#Open alert window
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(5)
driver.switch_to.alert 

