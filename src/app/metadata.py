"""CHANGES IN THIS FILE CAN LEAD TO ADVERSE EFFECTS AND CAN EVEN CRASH THE APPLICATION"""

import os
from typing import List

# App
NAME: str = "Smart Manager"
VERSION: str = "0.1.0-alpha"
WEBSITE: str = "https://jeeldobariya38.github.io/Smart-Manager/"
REPO: str = "https://github.com/JeelDobariya38/Smart-Manager"

# Paths (all path are relative to this file)
__DATADIR: list[str] = ["..", "..", "..", "data"]
__RESOURCEDIR: list[str] = ["..", "..", "..", "resource"]

# FilePath (Do Not Change this session, instead change above "Paths" session)
DATADIR_PATH: str = os.path.join(__file__, os.path.sep.join(__DATADIR)) + os.path.sep
RESOURCEDIR_PATH: str = os.path.join(__file__, os.path.sep.join(__RESOURCEDIR)) + os.path.sep

# For .EXE files
# DATADIR_PATH: str = os.path.join(__file__, os.path.sep.join(__DATADIR)) + os.path.sep
# RESOURCEDIR_PATH: str = os.path.join(__file__, os.path.sep.join(__RESOURCEDIR)) + os.path.sep

# App Configuration
DATA_SEPARATOR: str = " -> "
