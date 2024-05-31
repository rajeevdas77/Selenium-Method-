# Alert and pop 

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[1]").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(10)