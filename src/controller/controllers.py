from typing import Protocol
from abc import ABC, abstractmethod


class PrintAble(Protocol):
    def __repr__():
        ...


class Controller(ABC):
    @abstractmethod
    def getinput(self) -> str:
        pass

    @abstractmethod
    def showoutput(self, msg: str | PrintAble)-> None:
        pass


class CommandlineController(Controller):
    def __init__(self):
        pass
    
    def getinput(self) -> str:
        return input()

    def showoutput(self, msg: str | PrintAble = "")-> None:
        print(msg)
