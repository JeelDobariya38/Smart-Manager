from SmartManager.App import app  # noqa: F401, F403
from SmartManager.Database.localdriver import LocalDriver  # noqa: F401, F403


def app_run():
    app.init(LocalDriver())
    app.main()


if __name__ == "__main__":
    app_run()
