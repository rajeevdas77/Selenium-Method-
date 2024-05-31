from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# import driver
driver=webdriver.Edge()

# ser_obj=Service("C:\Ddrivers\chromedriver\chrome-win32\chrome-win32.exe")
# driver=webdriver.Chrome(service=ser_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window
import time
#1- Scrolling page
# driver.execute_script("window.scrollBy(0,4000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:",value)
# time.sleep(5)

#2- Scroll down page till the element is visible

# flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:",value)
# time.sleep(5)

#3- Scroll down page till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:",value)

# time.sleep(5)

#4- Scroll up to Starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number if pixels moved:",value)
time.sleep(5)