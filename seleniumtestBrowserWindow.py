from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#windowid=driver.current_window_handle
#print(windowid) #1584E89D9799DD6D0C870AF49A293AA7
#                #322DA683D7633FA453AE16BB65F94662

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click() 
windowsIds=driver.window_handles

#approh 1

# parentwindowsid=windowsIds[0]   
# childwindowid=windowsIds[1]

# print(parentwindowsid,childwindowid)
#         
# driver.switch_to.window(childwindowid)
# print("title of the child window",driver.title)

# driver.switch_to.window(parentwindowsid)
# print("title if the parent window", driver.title)

#Approch 2

# for winid in windowsIds:
#     driver.switch_to.window(winid)
#     print(driver.title)

