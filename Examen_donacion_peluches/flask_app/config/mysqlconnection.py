import os
from dotenv import load_dotenv
import pymysql.cursors

load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                db=db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
        except Exception as e:
            print("Error de conexión:", e)
            self.connection = None

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                try:
                    query = cursor.mogrify(query, data)
                    print("Running Query:", query)
                    
                    cursor.execute(query, data)
                    
                    if query.lower().find("insert") >= 0:
                        self.connection.commit()
                        return cursor.lastrowid
                    elif query.lower().find("select") >= 0:
                        result = cursor.fetchall()
                        return result
                    else:
                        self.connection.commit()
                        return True
                except Exception as e:
                    print("Query failed:", e)
                    return False
                finally:
                    cursor.close()
        except Exception as e:
            print("Connection failed:", e)
            return False
        finally:
            if self.connection:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)
