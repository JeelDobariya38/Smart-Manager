from abc import ABC, abstractmethod
from typing import Protocol, Union


class PrintAble(Protocol):
    def __repr__(self) -> str:
        ...


class Controller(ABC):
    @abstractmethod
    def get_input(self) -> str:
        pass

    @abstractmethod
    def show_output(self, msg: Union[str, PrintAble] = "") -> None:
        pass


class CommandlineController(Controller):
    def __init__(self):
        pass

    def get_input(self) -> str:
        return input()

    def show_output(self, msg: Union[str, PrintAble] = "") -> None:
        print(msg)
