from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def root():
    return "Smart Manager: Securing Passwords, Streamlining Authentication"

@api.get("/info")
def info():
    return {
        "title": "Smart Manager",
        "subtitle": "Securing Passwords, Streamlining Authentication",
        "description": "Smart Manager is a Python command-line application designed to securely store and manage passwords and authentication-related data.",
        "url": "https://github.com/JeelDobariya38/Smart-Manager"
    }
