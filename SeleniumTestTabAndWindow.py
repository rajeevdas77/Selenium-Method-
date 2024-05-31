from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(5)

  #1)  Method1 Open new tap 
# regilink=Keys.CONTROL+Keys.RETURN
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)
# time.sleep(3)


  #2) Method2 Open a new tab And Switches to new tab
# driver.get("https://www.foundit.in/")
# driver.switch_to.new_window("tab")
# driver.get("https://demo.nopcommerce.com/")


#3)  Method3 Open a new browser window and switches to new window
driver.get("https://www.foundit.in/")
driver.switch_to.new_window("window")
driver.get("https://demo.nopcommerce.com/")
