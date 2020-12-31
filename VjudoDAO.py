import pymysql
import mysql.connector
import mydbconfig as cfg
class JudoDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=       cfg.mysql['host'],
        user=       cfg.mysql['user'],
        password=   cfg.mysql['password'],
        database=   cfg.mysql['database'],
        auth_plugin='mysql_native_password'
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into athlets (name, age, belt,  weight, gender) values (%s, %s, %s, %s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from athlets"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from athlets where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        #name, age, belt,  weight, gender
        sql="update athlets set name = %s, age=%s, belt=%s, weight=%s, gender=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from athlets where id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        #print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','name','age', "belt", "weight", "gender"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
judoDAO = JudoDAO()

