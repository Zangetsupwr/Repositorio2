import pymysql.cursors
import pymysql
from flask import Flask

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host='localhost',
                                     user='root', 
                                     password='root', 
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True)
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            query = cursor.mogrify(query, data) if data else query
            cursor.execute(query)
            return cursor.fetchall() if query.lower().strip().startswith("select") else None

def connectToMySQL(db):
    return MySQLConnection(db)
