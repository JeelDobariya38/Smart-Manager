from .controller import Controller

CONTROLLER: Controller = Controller()


def init(dbdriver) -> None:
    CONTROLLER.set_db_driver(dbdriver)


def main() -> None:
    CONTROLLER.run()
    CONTROLLER.welcome()
    while CONTROLLER.isrunning():
        command = CONTROLLER.get_command()
        CONTROLLER.execute_command(command)
