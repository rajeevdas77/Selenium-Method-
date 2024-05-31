from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# driver. find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[2]/div[2]/div/div/div/a/span").click()
# time .sleep(10)
# driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[1]/input").send_keys("7008478833")
# driver. find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[2]/div/form/div[3]/button").click()
# time.sleep(10)
driver.find_element(By.XPATH,"//span[contains(text(),'Mobiles')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//img[@alt='Realme']").click()
time.sleep(5)
print(driver.title)

