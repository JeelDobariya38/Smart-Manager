from typing import Protocol
from abc import ABC, abstractmethod


class PrintAble(Protocol):
    def __repr__():
        ...


class Controller(ABC):
    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def show_output(self, msg: str | PrintAble) -> None:
        pass


class CommandlineController(Controller):
    def __init__(self):
        pass

    def get_input(self) -> str:
        return input()

    def show_output(self, msg: str | PrintAble = "") -> None:
        print(msg)