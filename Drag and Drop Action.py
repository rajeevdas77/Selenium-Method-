##Drag-Drop Action

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Edge()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

sourec_element=driver.find_element(By.XPATH,"//*[@id='box6']")
target_element=driver.find_element(By.XPATH,"//*[@id='box106']")

actions=ActionChains(driver)
actions.drag_and_drop(sourec_element , target_element).perform()
time.sleep(5)
print(driver.title)

