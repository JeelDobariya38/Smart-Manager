import sqlite3


class SqliteDriver:
    def __init__(self, databasepath):
        self.database_path = databasepath
        self.initlize_database()
    
    def initlizeddatabase(self):
        db = sqlite3.connect(self.database_path)
        db.close()
    
    def execute_sql(self, sql_query) -> None:
        return
