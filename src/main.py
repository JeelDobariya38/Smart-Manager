from . import App

import sys
import os

def resolve_path():
    sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    resolve_path()
    app.init()
    app.main()
