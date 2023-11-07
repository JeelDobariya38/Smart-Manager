from app import commands
from app.input_handler import InputHandler

def init() -> None:
    print("Welcome to Smart Manager Application")
    print()

def main(inputhandler: InputHandler) -> None:
    while True:
        inp = inputhandler.input(">> ").strip().lower()
        
        if inp == "":
            continue

        if inp == "quit" or inp == "exit":
            print("Quitting the app...")
            return
        
        if inp == "help":
            commands.print_help_message()
            continue

        if inp in ["write", "save"]:
            commands.writepassword()
            continue
        
        print("Invalid Input!!!")
        print()

if __name__ == "__main__":
    init()
    main(InputHandler())
