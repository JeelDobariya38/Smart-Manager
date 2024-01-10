from abc import ABC, abstractmethod
from typing import Self


class CommandInterface(ABC):
    @abstractmethod
    def convert_to_command(self, textrepr: str) -> Self:
        pass

    @abstractmethod
    def match(self, textrepr: str) -> bool:
        pass

    @abstractmethod
    def execute(self, controller) -> None:
        pass


class Command(CommandInterface):
    commands: Self = []

    def convert_to_command(self, textrepr: str) -> Self:
        textrepr = textrepr.lower()
        for command in self.commands:
            if command.match(textrepr):
                return command
        raise ValueError("Not a valid text representaion of Command!!")

    @staticmethod
    def add(command: CommandInterface) -> None:
        Command.commands.append(command)

    def match(self, textrepr: str) -> bool:
        return False

    def execute(self, controller) -> None:
        pass


class InvalidCommand(Command):
    def match(self, textrepr: str) -> bool:
        return True

    def execute(self, controller):
        controller.userinterface.show_output("Invaild Command!!")


class WelcomeCommand(Command):
    def match(self, textrepr: str) -> bool:
        return True

    def execute(self, controller):
        controller.userinterface.show_output("Welcome To Smart Manager")


class QuitCommand(Command):
    def match(self, textrepr: str) -> bool:
        return textrepr in ["quit", "exit"]

    def execute(self, controller):
        controller.userinterface.show_output("Quitting the application...")
        controller.quit()


Command.add(QuitCommand())
