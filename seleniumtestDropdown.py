from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Edge()
driver.get("https://www.opencart.com/index.php?route=account/register")
dropcuntry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
#Select option for Dropdown
# dropcuntry.select_by_visible_text("India")
# dropcuntry.select_by_value("10")
# dropcuntry.select_by_index("14")

#capture all the option and print them
alloption=dropcuntry.options
print("total number of option:",len(alloption))

for opt in alloption:
    print(opt.text)

