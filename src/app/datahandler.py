from . import metadata

DATA_FILE = metadata.DATADIR_PATH + "data.txt"

def save_data(website, password):
    data = metadata.DATA_SEPARATOR.join([website, password])
    with open(DATA_FILE, "a") as f:
        f.write(data + '\n')

def load_data():
    data_list = []
    with open(DATA_FILE) as f:
        data = f.read()
        for dataitem in data.split("\n"):
            data_list.append(dataitem.split(metadata.DATA_SEPARATOR))
    return data_list[:-1]
