#How to prefrom Scrolling and DropDown
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium . webdriver.support.select import Select
from selenium . webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
#Scrolling
driver.execute_script("window.scrollBy(0,800)","")
value = driver.execute_script("return window.pageYOffset;")
print("Number if pixels moved:",value)
time.sleep(5)
#DropDown
dropcuntry=Select(driver.find_element(By.XPATH,"//*[@id='country']"))
time.sleep(5)
dropcuntry.select_by_visible_text("India")
time.sleep(5)
