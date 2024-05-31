from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time

driver.get("https://money.rediff.com/index.html")
driver.maximize_window

#Self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'YES Bank Ltd.')]/self::a").text()
# print(text_msg)

#Parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'YES Bank Ltd.')]/parent::li").text()
# print(text_msg)

#Child
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'YES Bank Ltd.')]/ancestor::li/child::ul").text()

#Ancestor
text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'YES Bank Ltd.')]/ancestor::li/child::ul").text()


time.sleep(5)


