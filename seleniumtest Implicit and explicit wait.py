# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj2hMP2tvf_AhWYZt4KHTJ-CJ8QPAgJ")
# driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("selenium")
# time.sleep(8)
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()


from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Edge()
driver.get("https://www.geeksforgeeks.org/python-add-the-element-in-the-list-with-help-of-indexing/?ref=lbp#practice")
try:
    element=WebDriverWait(driver,0).until(
        EC.presence_of_all_elements_located((By.XPATH,"//div[@class='sideBar--wrap']//a[normalize-space()='Python | Create list of numbers with given range']"))
    )
finally:
    driver.close()    