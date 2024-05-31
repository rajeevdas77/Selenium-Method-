from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver= webdriver.Edge()
# serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# time.sleep(5)
driver.implicitly_wait(15)
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
coutrieslist=driver.find_element(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(coutrieslist)
# time.sleep(5)

for country in coutrieslist:
    if country.text=="India":
        country.click()
        break
    
# time.sleep(10)

