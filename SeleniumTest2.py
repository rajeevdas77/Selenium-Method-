from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
d=webdriver.Chrome(service=serv_obj)
d.get ("http://www.automationpractice.pl/index.php")
d.maximize_window()

slidesr=d.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(slidesr))

links=d.find_elements(By.TAG_NAME,"a")
print(len(links))

time.sleep(5)