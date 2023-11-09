"""CHANGES IN THIS FILE CAN LEAD TO ADVERSE EFFECTS AND CAN EVEN CRASH THE APPLICATION"""  # noqa: E501

import os
from typing import List


if __name__ == "__main__":
    print("This script is not intended for direct execution,")
    input("Please use 'main.py' to launch the application.")
    quit()


# App
NAME: str = "Smart Manager"
VERSION: str = "v2.0.0-Beta"
WEBSITE: str = "https://jeeldobariya38.github.io/Smart-Manager/"
REPO: str = "https://github.com/JeelDobariya38/Smart-Manager"

# Paths (all path are relative to this file)
__DATADIR: List[str] = ["..", "..", "..", "data"]
__RESOURCEDIR: List[str] = ["..", "..", "..", "resource"]

# FilePath (Do Not Change this session, instead change above "Paths" session)
datadir_str: str = os.path.sep.join(__DATADIR)
resourcedir_str: str = os.path.sep.join(__RESOURCEDIR)

# For .Py Scripts
DATADIR_PATH: str = os.path.join(__file__, datadir_str) + os.path.sep
RESOURCEDIR_PATH: str = os.path.join(__file__, resourcedir_str) + os.path.sep

# For .EXE files
# DATADIR_PATH: str = os.path.join(__file__, datadir_str) + os.path.sep
# RESOURCEDIR_PATH: str = os.path.join(__file__, resourcedir_str) + os.path.sep

# App Configuration
DATA_SEPARATOR: str = " -> "
