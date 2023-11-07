def print_help_message():
    print("Here are valid commands:")
    print(" - \"quit\" or \"exit\": for quiting the app")
    print(" - \"read\" or \"load\": for reading or loading the existing passwords")
    print(" - \"write\" or \"save\": for writing or saveing the new passwords")
    print()

def writepassword():
    website = input("Enter a website: ")
    pasword = input("Enter a password: ")
    print(website + " -> " + pasword)
    print("operation successfull!!!")
    print()
