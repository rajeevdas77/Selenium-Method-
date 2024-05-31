from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium. webdriver.common.by import By
import time
driver= webdriver.Edge()
driver.get("https://paytm.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='app']/header/div/div[2]/div").click()

# driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div/iframe"))
# driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='app']/div[1]"))
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div/a/img").click()


