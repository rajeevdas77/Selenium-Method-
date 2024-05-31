##How to handle windows

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle) #A01FE79B86041F1AC790200618D76D8B
time.sleep(5)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle) #B1C8D73C018B6CA083DADFB3014B7D63
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()  #close only perant window

driver.quit()        