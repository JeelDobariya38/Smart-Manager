from pydevtools.output import output
from pyfilehandling import fileio

from app import eventhandler
from app import metadata

if __name__ == "__main__":
    print("This script is not intended for direct execution,")
    input("Please use 'main.py' to launch the application.")
    quit()


def init() -> None:
    fileio.create_dir(metadata.DATADIR_PATH)

    print(f"Welcome to {metadata.NAME} Application")
    print()


def main() -> None:
    while True:
        inp = input(">> ").strip().lower()

        if inp == "":
            continue

        if inp in ["quit", "exit"]:
            eventhandler.handle_quit_event()
            return

        if inp in ["info"]:
            eventhandler.handle_info_event()
            continue

        if inp in ["help"]:
            eventhandler.handle_help_event()
            continue

        if inp in ["write", "save"]:
            eventhandler.handle_write_password_event()
            continue

        if inp in ["read", "load"]:
            eventhandler.handle_read_password_event()
            continue

        output.print_warning("Invalid Input!!!")
        print()
