import os
import sys


if os.path.dirname(__file__) not in sys.path:
    sys.path.insert(0, os.path.dirname(__file__))


# Running The Actual Application
from controller import CommandlineController
from smartmanager import App


def main() -> None:
    controller = CommandlineController()
    app = App(controller)
    app.init()
    app.main()


if __name__ == "__main__":
    main()
