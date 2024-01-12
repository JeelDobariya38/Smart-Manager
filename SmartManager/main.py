from App import app  # noqa: F401, F403
from Api import api  # noqa: F401, F403
from Database.sqlitedriver import SqliteDriver  # noqa: F401, F403

import uvicorn

def get_database_path():
    return ""

def api_run(hostaddress: str = "127.0.0.1", portno: int = 8000):
    uvicorn.run(app=api, host=hostaddress, port=portno)


def app_run():
    app.init(SqliteDriver(get_database_path()))
    app.main()


if __name__ == "__main__":
    app_run()
