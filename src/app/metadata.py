"""CHANGES IN THIS FILE CAN LEAD TO ADVERSE EFFECTS AND CAN EVEN CRASH THE APPLICATION"""

import os

# App
NAME = "Smart Manager"
VERSION = "0.1.0-alpha"
WEBSITE = "https://jeeldobariya38.github.io/Smart-Manager/"
REPO = "https://github.com/JeelDobariya38/Smart-Manager"

# Paths (all path are relative to this file)
__DATADIR = ["..", "..", "..", "data"]
__RESOURCEDIR = ["..", "..", "..", "resource"]

# FilePath (Do Not Change this session, instead change above "Paths" session)
DATADIR_PATH = os.path.join(__file__, os.path.sep.join(__DATADIR)) + os.path.sep
RESOURCEDIR_PATH = os.path.join(__file__, os.path.sep.join(__RESOURCEDIR)) + os.path.sep

# App Configuration
DATA_SEPARATOR = " -> "
