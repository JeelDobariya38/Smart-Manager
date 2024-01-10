from typing import Protocol


class UserInterface(Protocol):
    def get_input(self, msg: str = "") -> str:
        ...

    def show_output(self, msg: str) -> None:
        ...


class CLI:
    def __init__(self):
        pass

    def get_input(self, msg: str = "") -> str:
        return input(msg)

    def show_output(self, msg: str) -> None:
        print(msg)
