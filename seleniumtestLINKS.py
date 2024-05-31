from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads ").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# Find number of links in pages
# links=driver.find_elements(By.TAG_NAME,"a")
links=driver.find_elements(By.XPATH,"//a")
print("total number of links:", len(links))

#Print all the link Names
for link in links:
    print(link.text)


time.sleep(10)

