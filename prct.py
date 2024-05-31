# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time


# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver_win32 (3)")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(10)
 

# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# # driver.find_element(By.XPATH,"//*[@id='txtCaptcha']").send_keys("3663")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# time.sleep(10)


# 

### Kotak
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver= webdriver.Edge()
# driver.get("https://www.kotak.com/en/home.html") 
# driver.maximize_window()
# driver.implicitly_wait(5)
# login=driver.find_element(By.XPATH,"//a[@class = 'trk-login-net btn btn-primary login-link-attr']")
# login.click()
# handles=[]
# handles=driver.window_handles
# for handle in handles:
#     print(handle)

##How to handle windows

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Edge()

# driver.get("https://demo.automationtesting.in/Windows.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
# print(driver.current_window_handle) #A01FE79B86041F1AC790200618D76D8B
# time.sleep(5)
# handles=driver.window_handles
# for handle in handles:
#     driver.switch_to.window(handle) #B1C8D73C018B6CA083DADFB3014B7D63
#     print(driver.title)
#     if driver.title=="Frames & windows":
#         driver.close()  #close only perant window

# driver.quit()   

###How to hendle Alerts

# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException



# from selenium. webdriver.common.by import By
# import time
# driver=webdriver.Edge()
# driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//input[@ type='submit']").click()
# time.sleep(5)
 
# #Switch the control to the Alert window

# obj = driver.switch_to.alert
# #Retrieve the message on the Alert window
# msg=obj.text
# print ("Alert shows following message: "+ msg )
# time.sleep(10)
# #use the accept() method to accept the alert
# obj.accept()
# print(" Clicked on the OK Button in the Alert Window")
# driver.close
# driver.find_element(By.XPATH,"//input[@ type='text']").send_keys("selenium")
# time.sleep(5)


# screenshot
# from lib2to3.pgen2 import driver
# from selenium import webdriver 
# from time import sleep 
# driver= webdriver.Edge() 
# driver.get("https://mail.google.com/mail/u/0/#inbox") 
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get_screenshot_as_file("google.png")
# driver.quit()
# print("end...")

#How to prefrom Scrolling and DropDown

# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium . webdriver.support.select import Select
# from selenium . webdriver.common.by import By
# import time
# driver=webdriver.Edge()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# #Scrolling
# driver.execute_script("window.scrollBy(0,800)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:",value)
# time.sleep(5)
# #DropDown
# dropcuntry=Select(driver.find_element(By.XPATH,"//*[@id='country']"))
# time.sleep(5)
# dropcuntry.select_by_visible_text("India")
# time.sleep(5)

##Window Popup Handle and Mouse hover handle
# from lib2to3.pgen2 import driver
# from tkinter import E
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium . webdriver.support.select import Select
# import time
# driver=webdriver.Edge()
# driver.get("https://testsigma.com/blog/mouse-hover-in-selenium/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# #window popup handle
# driver.find_element(By.XPATH,"//*[@id='hs-eu-decline-button']").click()
# time.sleep(5)
# #Mouse Hover Action
# product=driver.find_element(By.XPATH,"//*[@id='__next']/header/div/div/nav/ul[1]/li[2]/span")
# action=ActionChains(driver)
# action.move_to_element(product).perform()
# time.sleep(4)

##Double Click Action
# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
# driver=webdriver.Edge()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# #Scroll page
# driver.execute_script("window.scrollBy(0,100)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:",value)
# time.sleep(5)
# #Double Click
# button=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
# act=ActionChains(driver)
# act.double_click(button).perform()
# time.sleep(4)

##Drag-Drop Action

# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium .webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver=webdriver.Edge()
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()

# sourec_element=driver.find_element(By.XPATH,"//*[@id='box6']")
# target_element=driver.find_element(By.XPATH,"//*[@id='box106']")

# actions=ActionChains(driver)
# actions.drag_and_drop(sourec_element , target_element).perform()
# time.sleep(5)
# print(driver.title)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Edge()
driver.get("https://www.tutorialspoint.com/index.htm")
driver.maximize_window()

cookies=driver.get_cookies()
print(len(cookies))#print number of cookies 
print(cookies)#print a cookires in paires

#How to add a cookies
cookies={"name","age","element","value"}
driver.add_cookie(cookies)
print(len(cookies))


