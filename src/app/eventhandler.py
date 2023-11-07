from . import commands

def handle_quit_event():
    commands.quit_appplication()

def handle_help_event():
    commands.print_help_message()

def handle_write_password_event():
    commands.write_password()

def handle_read_password_event():
    commands.read_password()

def handle_info_event():
    commands.read_info()
