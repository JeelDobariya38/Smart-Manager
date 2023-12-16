import sys
import os

if os.path.dirname(__file__) not in sys.path:
    sys.path.insert(0, os.path.dirname(__file__))

from SmartManager import App


def main():
    app = App()
    app.init()
    app.main()


if __name__ == "__main__":
    main()
