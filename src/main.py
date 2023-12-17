import sys
import os


if os.path.dirname(__file__) not in sys.path:
    sys.path.insert(0, os.path.dirname(__file__))


# Running The Actual Application
from smartmanager import App
from controller import CommandlineController


def main():
    controller = CommandlineController()
    app = App(controller)
    app.init()
    app.main()


if __name__ == "__main__":
    main()
