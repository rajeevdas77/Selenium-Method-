from selenium import webdriver
from selenium .webdriver.common .by import By
def test_search_for_a_valid_product():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME,"//input[@type=('text')]").send_keys("HP")
    driver.find_element(By.CLASS_NAME,"//button[@class='btn btn-default btn-lg']").click()