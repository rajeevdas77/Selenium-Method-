from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\Resume1.pdf")
time.sleep(10)