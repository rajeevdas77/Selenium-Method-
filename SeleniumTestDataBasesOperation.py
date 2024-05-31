import mysql.connector
con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="Rajeev123#",database="collage")
curs=con.cursor()
curs.execute("insert into students values (4,'raja',25,'MP','2003-9-09','Mech',500)")
con.commit()
con.close()
print("finished")

