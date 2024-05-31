# # from selenium import webdriver
# # # driver = webdriver.Chrome('C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe')
# # # driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# # from selenium.webdriver.chrome.service import Service
# #
# # ser_obj=Service(r"C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# # driver=webdriver.Chrome(service=ser_obj)
# # driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# # # driver.impicitly_wait(30)
#
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time
#
# serv_obj=Service("C:\Ddrivers\chromedriver_win32 (1)\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# time.sleep(5)
# regilink=Keys.CONTROL+Keys.RETURN
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)
# time.sleep(3)



# import openpyxl
# #flie--->workbook----->sheets----->rows---->cells
# file="D:\Selenium Automation\screenshot\Book1.xlsx"
# workbook=openpyxl.load_workbook(file)
# sheet=workbook["sheet1"]
# row=sheet.max_row
# cols=sheet.max_column
# for r in range(1,row+1):
#     for c in range(1,cols+1):
#         print(sheet.cell(r,c).value,end='       ')
#     print()


# insert_query="insert into students values (3,'ram',24,'RJ','2003-10-03','Mech',200)"
# update_query="update students set Name='bikky' where Rollno=3";
# delete_query="delete from students where Rollno=3";
#
#
# import mysql.connector
#
# con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="Rajeev123#",database="collage")
# curs=con.cursor()
# curs.execute(delete_query)
# con.commit()
# con.close()
# print("finished")

import mysql.connector
try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="Rajeev123#", database="collage")
    curs=con.cursor()
    curs.execute("select*from students")

    for row in curs:
        print((row[0],row[1],row[2]))
    con.close()

except:
    print("Connection unsuccessfull...")

print("Finished")
