# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# driver.switch_to.default_content()

# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT,"/html/body/main/ul/li[679]/a/span").click()
# driver.switch_to.default_content()

# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATHT,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()


#InnerIframe

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("RAJEEV") 