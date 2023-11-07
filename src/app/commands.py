from . import metadata

def quit_appplication():
    print("Quiting the Application....")

def print_help_message():
    print("Here are valid commands:")
    print(" - \"quit\" or \"exit\": for quiting the app")
    print(" - \"read\" or \"load\": for reading or loading the existing passwords")
    print(" - \"write\" or \"save\": for writing or saveing the new passwords")
    print()

def write_password():
    website = input("Enter a website: ")
    pasword = input("Enter a password: ")
    print(website + " -> " + pasword)
    print("operation successfull!!!")
    print()

def read_password():
    pass

def read_info():
    path = metadata.RESOURCEDIR_PATH + "info.txt"
    with open(path) as f:
        data = f.read()
    print(data)
