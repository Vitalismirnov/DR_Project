import pymysql
import mysql.connector


db = pymysql.connect(
    host="localhost", 
    user = "root", 
    password = "xxxx",
    )


mycursor = db.cursor() 
# create a new DB, called judo
#first check if exists (drop), then create
mycursor.execute("DROP DATABASE IF EXISTS judo");
mycursor.execute("CREATE DATABASE judo");
mycursor.execute("USE judo");

mycursor.execute("CREATE TABLE athlets (id int auto_increment primary key, \
                    name varchar(250), \
                    age int, \
                    belt ENUM('white', 'red', 'yellow', 'orange', 'green', 'blue', 'brown'), \
                    weight float, \
                    gender ENUM('male', 'female', 'other')\
               )");
               

sql=("insert into athlets (name, age, belt,  weight, gender ) values (\"John Gray\", \"22\",  \"red\", \"90.5\", \"male\")")

mycursor.execute(sql)
db.commit()
myresult = mycursor.fetchall()

for x in myresult:
  print(x) 