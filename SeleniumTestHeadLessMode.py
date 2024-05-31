# It is only works on Bekent
from selenium import webdriver
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    sev_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=sev_obj,options=ops)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()