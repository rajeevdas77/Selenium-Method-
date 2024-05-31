from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32 (1)\chromedriver.exe")
# driver.implicitly_wait(60)

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element("q").send_keys("songs")
time.sleep(15000)
driver.find_element("btnK").click()
# driver.close()
# driver.quit()

print("Test completed")