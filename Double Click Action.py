##Double Click Action
# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
# driver = webdriver.Chrome()
from gettext import install
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
import time
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.execute_script("window.scrollBy(0,100)","")
value = driver.execute_script("return window.pageYOffset;")
print("Number if pixels moved:",value)
time.sleep(5)
button=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
act=ActionChains(driver)
act.double_click(button).perform()
time.sleep(4)