from fastapi import FastAPI

from .databaseinfo import DatabaseInfo

import os
import json

DATABASE_INFO = DatabaseInfo()
api = FastAPI()


@api.get("/")
def root():
    return "Smart Manager: Securing Passwords, Streamlining Authentication"


@api.get("/info")
def info():
    file_path = os.path.dirname(__file__)
    path = os.path.join(file_path, '..', '..', 'smart_manager_config.json')
    return json.load(open(path))
