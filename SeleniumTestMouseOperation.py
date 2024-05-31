# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window
# import time
#Login
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
#Admin---> User Managment----->User
# driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul")

#1) MouseHover action -------------------Fst import--> from selenium.webdriver import ActionChains
# act=ActionChains(driver)
# act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()


#2) Right click Action

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window
# import time

# button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
# time.sleep(3)
# act=ActionChains(driver)
# act.context_click(button).perform()    #Right Click
# time.sleep(5)


#3) Double Click Action

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service

# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
# driver.maximize_window
# import time
# driver.switch_to.frame("iframeResult")   #switch to frame
# field1=driver.find_element(By.XPATH,"//input[@id='field1']")
# field1.clear()
# field1.send_keys("RAJEEV")
# time.sleep(3)
# butoon=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# act=ActionChains(driver)
# act.double_click(butoon).perform()   # Double Click

# time.sleep(5)



#4) Drag and Drop Action 

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service

# ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window
# import time

# source_ele=driver.find_element(By.ID,"box4")
# target_ele=driver.find_element(By.ID,"box104")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# source_ele=driver.find_element(By.ID,"box6")
# target_ele=driver.find_element(By.ID,"box106")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# source_ele=driver.find_element(By.ID,"box1")
# target_ele=driver.find_element(By.ID,"box101")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# source_ele=driver.find_element(By.ID,"box2")
# target_ele=driver.find_element(By.ID,"box102")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# source_ele=driver.find_element(By.ID,"box3")
# target_ele=driver.find_element(By.ID,"box103")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# source_ele=driver.find_element(By.ID,"box5")
# target_ele=driver.find_element(By.ID,"box105")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# source_ele=driver.find_element(By.ID,"box7")
# target_ele=driver.find_element(By.ID,"box107")
# act=ActionChains(driver)
# act.drag_and_drop(source_ele,target_ele).perform()

# time.sleep(3)


#5) Slider Action


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

ser_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window
import time

min_slider=driver.find_element(By.XPATH,"//span[1]")
max_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Location of sliding Before moving..... ")
print(min_slider.location)   #{'x': 59, 'y': 250}
print(max_slider.location)   #{'x': 412, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of sliding After moving..... ")
print(min_slider.location)  #{'x': 158, 'y': 250}
print(max_slider.location)  #{'x': 374, 'y': 250}