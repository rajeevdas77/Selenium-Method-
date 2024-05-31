from lib2to3.pgen2 import driver
from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium . webdriver.support.select import Select
import time
driver=webdriver.Edge()
driver.get("https://testsigma.com/blog/mouse-hover-in-selenium/")
driver.maximize_window()
driver.implicitly_wait(10)
#window popup handle
driver.find_element(By.XPATH,"//*[@id='hs-eu-decline-button']").click()
time.sleep(5)
#Mouse Hover Action
product=driver.find_element(By.XPATH,"//*[@id='__next']/header/div/div/nav/ul[1]/li[2]/span")
action=ActionChains(driver)
action.move_to_element(product).perform()
time.sleep(4)