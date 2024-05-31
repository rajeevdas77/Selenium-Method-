# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://testautomationpractice.blogspot.com/")
# # STATIC
#1) Count number of row & colums

# noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# noOfColums=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))

# print(noOfRows)
# print(noOfColums)

#2) Read specific row & colum data

# data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

#3) Read all the rows & Colums data

# print("Printing all the rows and colums data :-")

# for r in range (2,noOfRows+1):
#     for c in range(1,noOfColums+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='         ')
#     print()

#4) Read data base on condition (List book name whose author is mukesh) 

# for r in range(2,noOfRows+1):
#     authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
#     if authorName=="Mukesh":
#         bookName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) + "]/tb[1]").text
#         price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) + "]/tb[4]").text
#         print(bookName,"        ",authorName,"      ",price)     


# driver.close 


#DYNAMIC WEBTABLE

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


#ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.chrome("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Login

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(10)

#Admin---> User Managment----->User

driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul")


