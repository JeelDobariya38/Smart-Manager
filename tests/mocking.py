from src.controller import Controller, PrintAble

from typing import List, Union


class NoMoreMockInputsException(Exception):
    def __init__(self, message="No more mock inputs available. Please add more mock inputs for testing!!!"):
        self.message = message
        super().__init__(self.message)


class MockController(Controller):
    def __init__(self):
        self.inputs = []

    def set_inputs(self, inputs: List[str]):
        self.inputs = inputs

    def get_input(self) -> str:
        if len(self.inputs) == 0:
            raise NoMoreMockInputsException()
        else:
            self.inputs.pop(0)

    def show_output(self, msg: Union[str, PrintAble] = "") -> None:
        print(msg)
