from selenium import webdriver
driver=webdriver.Chrome()
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# sev_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=sev_obj)

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window

#Relative Xpath
# driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("T-shirt")
# driver.find_element(By.XPATH,"//button[@name='submit_search']").click()

#OR Xpath
# driver.find_element(By.XPATH,"//input[@id'search_query_top' or @ name='search_query']").send_keys("t-shirt")
# driver.find_element(By.XPATH,"//button[@name='submit_search' and @ class='btn btn-default button-search' ]").click()

#Contains()  &  Start_With()
# driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("t-shirt")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit')]").click()

#Text()
driver.find_element(By.XPATH,"//a[text()='Woman']").click()
time.sleep(5)


