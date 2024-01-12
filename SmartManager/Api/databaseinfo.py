class DatabaseInfo:
    def __init__(self):
        self.databasepath = ""

    def set_database_path(self, path: str) -> None:
        self.databasepath = path

    def get_databasepath(self) -> str:
        return self.databasepath
