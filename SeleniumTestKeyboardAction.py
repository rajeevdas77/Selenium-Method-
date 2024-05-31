from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://text-compare.com/")
driver.maximize_window

import time

driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("Welcome Rajeev")
driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

act=ActionChains(driver)

act.key_down(Keys.Control).send_keys("a").key_up(Keys.Control).perform()
time.sleep(2)
act.key_down(Keys.Control).send_keys("c").key_up(Keys.Control).perform()
time.sleep(2)
act.send_keys(Keys.TAB).perform()
time.sleep(2)
act.key_down(Keys.Control).send_keys("v").key_up(Keys.Control).perform()

time.sleep(5)


