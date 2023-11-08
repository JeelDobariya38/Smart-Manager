from pydevtools.output import output

from datahandler import datahandler
from app import metadata

def quit_appplication() -> None:
    print("Quiting the Application....")


def print_help_message() -> None:
    print("Here are valid commands:")
    print(" - \"quit\" or \"exit\": for quiting the app")
    print(" - \"read\" or \"load\": for reading the existing passwords")
    print(" - \"write\" or \"save\": for writing the new passwords")
    print()


def write_password() -> None:
    website = input("Enter a website: ")
    password = input("Enter a password: ")
    datahandler.save_data(website, password)
    output.print_output("saved successfull!!!", "green")
    print()


def read_password() -> None:
    data_list = datahandler.load_data()
    try:
        if len(data_list) == 0:
            output.print_warning("No Passwords to Show....")
            print()
            return

        for data_item in data_list:
            print(f"{data_item[0]} - {data_item[1]}")

        print()
    except IndexError as _:  # noqa: F841
        raise Exception("data is corrupted!!")


def read_info() -> None:
    path = metadata.RESOURCEDIR_PATH + "info.txt"
    with open(path) as f:
        data = f.read()
    print(data)


if __name__ == "__main__":
    input("This script is not intended to be run directly. Please run 'main.py' to start the application.")
