from controller import Controller

class App:
    def __init__(self, controller: Controller):
        self.controller = controller
    
    def init(self):
        pass

    def main(self):
        self.welcome()

    def quit(self):
        pass
    
    def welcome(self):
        self.controller.show_output("Welcome to Smart Manager Application")
        self.controller.show_output()
