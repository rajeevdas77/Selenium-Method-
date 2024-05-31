# import imp
# from lib2to3.pgen2 import driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Edge()
# driver.implicitly_wait(10)
# import time

# driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("rajeev")
# driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("das")
# driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("rajeevdas7733@gmail.com")
# driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("rajeev123@")
# driver.execute_script("window.scrollBy(0,350)","")
# value=driver.execute_script("returnwindow.pageYoffset;")
# time.sleep(6)
# driver.find_element(By.XPATH,"//input[@id='input-newsletter-yes']").click()
# driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
# time.sleep(8)


# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# driver=webdriver.Edge()
# import time

# driver.get("https://www.geeksforgeeks.org/python-interview-questions/?ref=lbp")
# driver.maximize_window()

# from ast import arguments
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Edge()
# import time
# driver.maximize_window()
# driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")


#scroll by Pixcel
# driver.execute_script("window.scrollBy(0,200)")
# time.sleep(5)

#scroll until the required
# specials_a= driver.find_element(By.LINK_TEXT,"Specials")
# driver.execute_script("arguments[0].scrollIntoView()",specials_a)
# time.sleep(5)

# contact_us= driver.find_element(By.LINK_TEXT,"Contact Us")
# driver.execute_script("arguments[0].scrollIntoview()",contact_us)
# time.sleep(5)

#how to hendal dynamic table

# import select
# from selenium import webdriver
# from selenium .webdriver.common.by import By
# driver=webdriver.Edge()
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# import time

from selenium import webdriver
from selenium .webdriver.common .by import By
def test_search_for_a_valid_product():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME,"//input[@type=('text')]").send_keys("HP")
    driver.find_element(By.CLASS_NAME,"//button[@class='btn btn-default btn-lg']").click()




