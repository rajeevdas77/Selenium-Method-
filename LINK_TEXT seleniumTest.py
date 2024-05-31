from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get ("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.ID,"small-searchterms").send_keys("Asus N551JK-XO076H Laptop")
# time.sleep(5)

# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()
time.sleep(5)
