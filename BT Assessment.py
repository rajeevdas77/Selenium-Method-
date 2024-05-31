import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
# ser_obj=Service("C:\Ddrivers\chromedriver\chromedriver-win64")

driver=webdriver.Edge()#service=ser_obj
import time
driver .get("https://www.bt.com/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.TAG_NAME,"div"))
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

time.sleep(10)

#use the accept() method to accept the alert
obj.accept()

print(" Clicked on the OK Button in the Alert Window")

driver.close
