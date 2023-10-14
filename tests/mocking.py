class MockInputHandler:
    def __init__(self,input: list):
        self.inp = input

    def input(self, prompt):
        print(prompt)
        if len(self.inp):
            return self.inp.pop()