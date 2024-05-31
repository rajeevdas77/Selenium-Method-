# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://jqueryui.com/datepicker/")
# driver.switch_to.frame(0) #switch of frame
# import time


#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/06/2012") #mm/dd/yyyy

# year = "2025"
# month = "March"
# date = "15"

# driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
# time.sleep(5)
# while True:
#     mo=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
#     yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

#     if mo==month and yr==year:
#         break
#     else:
#          driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #Next arrow
#          driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() #previos arrow
# time.sleep(5)


#select date

# dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
# for ele in dates:
#     if ele . text == date:
#         ele.click()
#         break

# time.sleep(3)






#Date of Birth

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
import select
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH,"//input[@id='dob']").click()  #open datepicker
#DropDown Method
datepicker_month=select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Dec")
time.sleep(2)

datepicker_year=select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1900")
time.sleep(5)

alldates=driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']")
for date in alldates:
    if date.text=="25":
       date.click()
       break
time.sleep(10)    





