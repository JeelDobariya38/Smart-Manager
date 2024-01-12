import sqlite3


class SqliteDriver:
    def __init__(self, databasepath):
        self.database_path = databasepath
        self.initlize_database()

    def initlize_database(self):
        db = sqlite3.connect(self.database_path)
        db.close()

    def setup(self):
        pass

    def execute_sql(self, sql_query) -> None:
        return
