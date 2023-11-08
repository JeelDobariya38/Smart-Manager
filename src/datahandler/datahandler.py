from app import metadata

from typing import List

DATA_FILE: str = metadata.DATADIR_PATH + "data.txt"


def save_data(website: str, password: str) -> None:
    data = metadata.DATA_SEPARATOR.join([website, password])
    with open(DATA_FILE, "a") as f:
        f.write(data + '\n')


def load_data() -> List[list[str]]:
    data_list = []
    try:
        with open(DATA_FILE) as f:
            data = f.read()
            if data == "":
                return []
            for dataitem in data.split("\n"):
                data_list.append(dataitem.split(metadata.DATA_SEPARATOR))
        return data_list[:-1]
    except FileNotFoundError as _:  # noqa: F841
        return []


if __name__ == "__main__":
    input("This script is not intended to be run directly. Please run 'main.py' to start the application.")