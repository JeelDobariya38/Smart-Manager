from App import app
from Database.localdriver import LocalDriver


def app_run():
    app.init(LocalDriver())
    app.main()


if __name__ == "__main__":
    app_run()
