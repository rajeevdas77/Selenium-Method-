from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium .webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://demo.opencart.com/admin/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("demo")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("demo")
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
time.sleep(10)
driver.find_element(By.CLASS_NAME,"btn-close").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Sales')]").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Orders')]").click()
time.sleep(3)

expected_customer_name="jeevitha nagarajan"
xpath_test="//form[@id='form-order']//tr//td[text()='"+expected_customer_name+"']"
driver.find_element(By.XPATH,xpath_test+"/preceding-sibling::td[3]").click()
time.sleep(5)

# expected_customer_name="maria maria"
# xpath_test="//form[@id='form-order']//tr//td[text()='"+expected_customer_name+"']"
# driver.find_element(By.XPATH,xpath_test+"/preceding-sibling::td[3]").click()
# time.sleep(5)

