from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Edge()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


#)--- How to handle Cookies
driver.add_cookie({"name","mycookies","value"})
cookies=driver.get_cookies()
print("size of cookies:",len(cookies))  #5 cookies
time.sleep(5)

#)  Print Details of all cookies
# for c in cookies:
#     print(c)
