from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests as requests

sec_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=sec_obj)
driver.get("http://www.deadlinkcity.com/")

alllinks=driver.find_elements(By.TAG_NAME,"a")
count=0

for link in alllinks:
    url=link.get_attribute('href')
    try:
       res=requests.head(url)
    except:
       None

    if res.status_code>400:
        print(url,"is brokem link")
        count=+1
    else:
        print(url,"is valid link")  
print("total number of broken links:",count)          
