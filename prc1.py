# from selenium import webdriver
# from selenium . webdriver.common.by import By
# driver=webdriver.Chrome("C:\Ddrivers\chromedriver_win32 (1)\chromedriver_win32 (3).exe")
# import time
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()

# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# time.sleep(10)


# from selenium import webdriver
# from selenium. webdriver. common.by import By
# from selenium. webdriver.chrome.service import Service
# import time
# ser_obj=Service("C:\Ddrivers\chromedriver\chromedriver_win32.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(10)

# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# time.sleep(10)
# PageTitle= driver.title
# print(PageTitle)
# driver.close()



# from selenium import webdriver
# from selenium . webdriver.common.by import By
# from selenium . webdriver.chrome.service import Service
# import time

# # ser_obj= Service("C:\Ddrivers\chromedriver\chromedriver_win32.exe")
# driver=webdriver.Edge()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(10)
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# time.sleep(10)

# PageTitle=driver.title
# print(PageTitle)

# driver.close()

# from selenium import webdriver 
# from selenium.webdriver.common .by import By
# from selenium.webdriver.chrome.service import Service

# ser_obj=Service("")
# driver=webdriver.Chrome(service=ser_obj)

# driver.get()


from selenium import webdriver
from selenium .webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='search']").send_keys("songs")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']//div").click()
time.sleep(5)