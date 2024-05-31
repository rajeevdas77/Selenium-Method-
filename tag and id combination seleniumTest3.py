from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

sev_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=sev_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

                 #tag and id combination
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("rajeev")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("rajeev")
                 #tag and class 
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("rajeev")    
                   #tag and attribute
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("rajeev")
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("rajeev")  
                      #tag, class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("rajeevdas123")       
time.sleep(5)                                      