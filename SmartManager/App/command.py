from abc import ABC, abstractmethod
from typing import Self, List


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
    commands: List[Self] = []

    def convert_to_command(self, textrepr: str) -> Self:
        textrepr = textrepr.lower()
        for command in self.commands:
            if command.match(textrepr):
                return command
        raise ValueError("Not a valid text representaion of Command!!")

    @staticmethod
    def add(command) -> None:
        Command.commands.append(command)  # type: ignore[misc]

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
        controller.userinterface.show_output()


class EmptyCommand(Command):
    def match(self, textrepr: str) -> bool:
        return textrepr == ""

    def execute(self, controller):
        pass

Command.add(EmptyCommand())


class QuitCommand(Command):
    def match(self, textrepr: str) -> bool:
        return textrepr in ["quit", "exit"]

    def execute(self, controller):
        controller.userinterface.show_output("Quitting the application...")
        controller.quit()

Command.add(QuitCommand())
