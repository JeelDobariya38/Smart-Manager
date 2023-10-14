# # Tests/conftest.py

import sys
import os

# Get the absolute path to the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))

# Add pydevtools to sys.path if it's not already there
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)
    sys.path.insert(1,os.path.dirname(__file__))