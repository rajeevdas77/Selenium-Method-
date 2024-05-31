from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

sev_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=sev_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#Select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()


checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxs))

#Select all the checkbox
# for i in range (len(checkboxs)):
#     checkboxs[i].click()

# Another method select aii the checkbox
for checkbox in checkboxs:
    checkbox.click()

#Select Multipale chechbox ex- Monday and Thursday
# for checkbox in checkboxs:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='thursday':
#         checkbox.click()

#Select last two checkbox
# for i in range (len(checkboxs)-3,len(checkboxs)):
#     checkboxs[i].click()

#Select first two checkbox
# for i in range (len (checkboxs)):
#     if i<3:
#         checkboxs[i].click()
time.sleep(5)
# Cleaing all the checkbox
for checkbox in checkboxs:
    if checkbox.is_selected():
        checkbox.click()




