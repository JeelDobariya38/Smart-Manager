from . import datahandler
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
    password = input("Enter a password: ")
    datahandler.save_data(website, password)
    print("operation successfull!!!")
    print()

def read_password():
    data_list = datahandler.load_data()
    try:
        for data_item in data_list:
            print(f"{data_item[0]} - {data_item[1]}")
    except IndexError as _:
        raise Exception("data is corrupted!!")

def read_info():
    path = metadata.RESOURCEDIR_PATH + "info.txt"
    with open(path) as f:
        data = f.read()
    print(data)
