
# # from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # driver=webdriver.Chrome()

# driver=webdriver.Edge()
# import time
# driver.get(://practice."httpssdetunicorns.com/")

# driver.maximize_window()
# time.sleep(5)
# # driver.switch_to.alert.dismiss()
# driver.find_element(By.XPATH,"//li[@id='menu-item-619']//a[normalize-space()='My account']").click()
# driver.execute_script("window.scrollBy(0,450)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number if pixels moved:",value)
# time.sleep(8)
# driver.find_element(By.XPATH,"//*[@id='username']").send_keys("rajeevdas")
# driver.find_element(By.XPATH,"//*[@id='password']").send_keys("kumarbdad123")
# driver.find_element(By.XPATH,"//*[@id='customer_login']/div[1]/form/p[3]/button").click()
# driver.close()

# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Edge()
# time .sleep(2)
# driver.get("https://practice.sdetunicorns.com/my-account/")
# driver.maximize_window()
# driver.execute_script("window.scrollBy(100,450)","")
# value=driver.execute_script("return window .pageyoffset;")
# print ("")
# time.sleep(5)
#get a title page
# PageTitle = driver.title
# print(PageTitle)
# act_title=driver.title
# exp_title="Practice E-Commerce Site » Comments Feed"
# if act_title==exp_title:
#     print("LoginTestPassed")
# else:
#     print ("loginTestFaild")
# driver.close()    

#Add number entered by user fixed
# def main():
#     a=input ('1st number')
#     b= input ('2nd number')
#     print (int (a) + int (b))
# main()    
       

val=input ("type in a number")
print(val)
print  (val.isdecimal())
print (val.isnumeric())

if val.isdecimal():
    num = int (val)
    print(num)