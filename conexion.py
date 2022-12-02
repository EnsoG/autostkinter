#py -m pip install mysql-connector
import mysql.connector

class DataBase():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='autosdb'
        )
        self.cursor = self.conn.cursor()