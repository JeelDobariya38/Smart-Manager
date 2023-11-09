from app import commands


if __name__ == "__main__":
    print("This script is not intended for direct execution,")
    input("Please use 'main.py' to launch the application.")
    quit()


def handle_quit_event() -> None:
    commands.quit_appplication()


def handle_help_event() -> None:
    commands.print_help_message()


def handle_write_password_event() -> None:
    commands.write_password()


def handle_read_password_event() -> None:
    commands.read_password()


def handle_info_event() -> None:
    commands.read_info()
