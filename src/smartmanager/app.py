from controller import Controller


class App:
    def __init__(self, controller: Controller):
        self.controller = controller

    def init(self) -> None:
        pass

    def main(self) -> None:
        self.welcome()

    def quit(self) -> None:
        pass

    def welcome(self) -> None:
        self.controller.show_output("Welcome to Smart Manager Application")
        self.controller.show_output()
