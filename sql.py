import pymysql

# Database creation: Image_Database
mydb = pymysql.connect(host='localhost', user='root', password='')
mycursor = mydb.cursor()
sql = "CREATE DATABASE IF NOT EXISTS Image_Database"
mycursor.execute(sql)
print("Database created successfully")

# Switch to the Image_Database
mydb = pymysql.connect(host='localhost', user='root', password='', database='Image_Database')
mycursor = mydb.cursor()

# Creating table: Image_path_Table
sql = "CREATE TABLE IF NOT EXISTS Image_path_Table (Name varchar(30), Image_Path varchar(100))"
mycursor.execute(sql)
mydb.commit()
print("Table created..")

# Inserting into the table
name = ['Ayisha','Abhinand','Obama','sachin']
path = [r'C:\Task\1. Attendence Marker\faces\Ayisha.jpg',
        r'C:\Task\1. Attendence Marker\faces\Abhinand.jpg',
        r'C:\Task\1. Attendence Marker\faces\obama.jpg',
        r'C:\Task\1. Attendence Marker\faces\sachin.jpg'
        ]

for i in range(len(name)):
    # Check if the data already exists
    check_sql = "SELECT * FROM Image_path_Table WHERE Name = %s AND Image_Path = %s"
    mycursor.execute(check_sql, (name[i], path[i]))
    existing_data = mycursor.fetchone()

    # If data doesn't exist, insert it
    if not existing_data:
        insert_sql = "INSERT IGNORE INTO Image_path_Table (Name, Image_Path) VALUES (%s, %s)"
        mycursor.execute(insert_sql, (name[i], path[i]))


mydb.commit()
print("Inserted the values successfully..")

# Selecting from table 
mydb = pymysql.connect(host='localhost', user='root', password='',database='Image_Database')
mycursor = mydb.cursor()
sql = "SELECT * FROM Image_path_Table"
mycursor.execute(sql)
result = mycursor.fetchall()

for row in result:
    name = row[0]
    path = row[1]
    print("Name",name,"Path",path)












# mydb = pymysql.connect(host='localhost', user='root', password='', database='Image_Database')
# mycursor = mydb.cursor()
# sql = "DROP DATABASE Image_Database"
# mycursor.execute(sql)
# mydb.commit
# print("Deleated..")