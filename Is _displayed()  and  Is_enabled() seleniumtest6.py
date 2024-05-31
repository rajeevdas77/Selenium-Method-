from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time

driver.get("https://demo.nopcommerce.com/p")
driver.maximize_window

# Is _displayed()  and  Is_enabled()

surchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Displaye ststes:",surchbox.is_displayed())
print("Enable states:",surchbox.is_enabled())

# Is_Selected() for radio button and check boxs

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//span[@class='female']")

print("default male radio button states....")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("After selecting male radio button")
print(rd_male.is_selected())
print(rd_female.is_selected())
time.sleep(5)