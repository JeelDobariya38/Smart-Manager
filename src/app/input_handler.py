class InputHandler:

    def __init__(self):
        pass

    def input(self, prompt: str) -> str:
        return input(prompt)

    def input_int(self, prompt: str) -> int:
        return int(input(prompt))
