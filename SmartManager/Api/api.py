from fastapi import FastAPI

from .databaseinfo import DatabaseInfo

DATABASE_INFO = DatabaseInfo()
api = FastAPI()


@api.get("/")
def root():
    return "Smart Manager: Securing Passwords, Streamlining Authentication"


@api.get("/info")
def info():
    return {
        "title": "Smart Manager",
        "subtitle": "Securing Passwords, Streamlining Authentication",
        "description": "Smart Manager is a Python command-line application designed to securely store and manage passwords and authentication-related data.",  # noqa: E501
        "url": "https://github.com/JeelDobariya38/Smart-Manager"
    }
