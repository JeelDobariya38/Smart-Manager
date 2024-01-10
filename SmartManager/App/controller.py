from SmartManager.App.interface import UserInterface, CLI
from SmartManager.App.command import (
    CommandInterface, Command, InvalidCommand, WelcomeCommand
)
from SmartManager.App.datahandler import Datahandler


class Controller:
    running = False
    datahandler: Datahandler = Datahandler()
    userinterface: UserInterface = CLI()
    command: CommandInterface = Command()

    def __init__(self):
        pass

    def set_db_driver(self, databasedriver):
        self.datahandler.databasedriver = databasedriver

    def isrunning(self) -> bool:
        return self.running

    def run(self) -> None:
        self.running = True

    def quit(self) -> None:
        self.running = False

    def welcome(self):
        WelcomeCommand().execute(self)

    def get_command(self) -> CommandInterface:
        textrepr = self.userinterface.get_input(">> ")
        try:
            return self.command.convert_to_command(textrepr)
        except ValueError as _:
            return InvalidCommand()

    def execute_command(self, command: CommandInterface):
        command.execute(self)
