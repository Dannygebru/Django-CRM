import mysql.connector

database = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     passwd = 'Ale16@2024'

)

#prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crm")

print("all is done")



