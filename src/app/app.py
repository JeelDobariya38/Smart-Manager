from . import eventhandler

def init() -> None:
    print("Welcome to Smart Manager Application")
    print()

def main() -> None:
    while True:
        inp = input(">> ").strip().lower()
        
        if inp == "":
            continue

        if inp == "quit" or inp == "exit":
            eventhandler.handle_quit_event()
            return
        
        if inp == "help":
            eventhandler.handle_help_event()
            continue

        if inp in ["write", "save"]:
            eventhandler.handle_write_password_event()
            continue

        if inp in ["read", "load"]:
            eventhandler.handle_read_password_event()
            continue
        
        print("Invalid Input!!!")
        print()
