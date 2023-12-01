import sqlite3 as sql

def db_connector(func, *args):
    def wapper():
        connection = sql.connect("database.db")
        cursor = connection.cursor()
        func(cursor, *args)
        connection.commit()
        connection.close()
    return wapper
