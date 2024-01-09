# conftest.py
import sys
import os


# Get the absolute path to the project directory
file_path = os.path.dirname(__file__)
path = os.path.join(file_path, '../src')
project_dir = os.path.abspath(path)


# Add pydevtools to sys.path if it's not already there
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)
    sys.path.insert(1, os.path.dirname(__file__))
    print("Resolveing Paths......")


def test_app():
    assert True
