#my Structured Query Language, CRUD- create, read, update, delete


import mysql.connector 

conn=mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydb"
)

mycursor=conn.cursor()
sql="INSERT INTO mydatabase1(st_name,st_email,st_mobile)VALUES('yuvraj','123@gmail.com','1234567890')"
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount,"row inserted.")


