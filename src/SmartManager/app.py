from controller import Controller

class App:
    def __init__(self, controller: Controller):
        self.controller = controller
    
    def init(self):
        pass

    def welcome(self):
        self.controller.showoutput("Welcome to Smart Manager Application")
        self.controller.showoutput()
    
    def main(self):
        self.welcome()
