from App import app  # noqa: F401, F403
from Api import api, DATABASE_INFO  # noqa: F401, F403
from Database.sqlitedriver import SqliteDriver  # noqa: F401, F403

import os
import uvicorn
import json


def get_config():
    file_path = os.path.dirname(__file__)
    path = os.path.join(file_path, '..', 'smart_manager_config.json')
    return json.load(open(path))

def get_databasepath():
    file_path = os.path.dirname(__file__)
    return os.path.join(file_path, "SmartManager.db")

def api_run(dbpath, hostaddress: str = "127.0.0.1", portno: int = 8000):
    DATABASE_INFO.set_database_path(dbpath)
    uvicorn.run(app=api, host=hostaddress, port=portno)


def app_run(dbpath):
    app.init(SqliteDriver(dbpath))
    app.main()


if __name__ == "__main__":
    config = get_config()
    databasepath = get_databasepath()
    print(config, databasepath)
    try:
        if config.get("api", False):
                apiconfg = config.get("api-config")
                api_run(databasepath, apiconfg["host"], apiconfg["port"])
        else:
            app_run(databasepath)
    except KeyError as e:
        raise ValueError("Config file is invalid!!")
