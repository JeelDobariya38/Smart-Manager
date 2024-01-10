from abc import ABC, abstractmethod
from typing import List


class CommandInterface(ABC):
    repr: str = ""
    hint: str = "Command class for Controlling other commands.."

    @abstractmethod
    def convert_to_command(self, textrepr: str) -> CommandInterface:
        pass

    @abstractmethod
    def match(self, textrepr: str) -> bool:
        pass

    @abstractmethod
    def execute(self, controller) -> None:
        pass


class Command(CommandInterface):
    repr: str = ""
    hint: str = "Command class for Controlling other commands.."
    commands: List[CommandInterface] = []

    def convert_to_command(self, textrepr: str) -> CommandInterface:
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


class HelpCommand(Command):
    repr: str = "help"
    hint: str = "For Showing Help Prompt"

    def match(self, textrepr: str) -> bool:
        return textrepr == "help"

    def execute(self, controller):
        msg = "Here is list of valid Commands:\n\n"
        msg += "Commands:\n"
        for command in self.commands:
            if command.repr != "":
                msg += f"    - {command.repr}: {command.hint}\n"
        controller.userinterface.show_output(msg)

Command.add(HelpCommand())


class QuitCommand(Command):
    repr: str = "quit"
    hint: str = "For Quitting The Application"

    def match(self, textrepr: str) -> bool:
        return textrepr in ["quit", "exit"]

    def execute(self, controller):
        controller.userinterface.show_output("Quitting the application...")
        controller.quit()

Command.add(QuitCommand())
