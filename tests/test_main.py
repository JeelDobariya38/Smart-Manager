from main import init, main
from mocking import MockInputHandler

def test_init(capfd):
    init()
    captured = capfd.readouterr()
    assert "Welcome to Smart Manager Application" in captured.out

class TestMain:
    def test_main_command_symbol(self, capfd) -> None:
        mock = MockInputHandler(["quit"])
        main(mock)
        captured = capfd.readouterr()
        assert ">>" in captured.out

    def test_main_quit_command(self, capfd) -> None:
        mock = MockInputHandler(["quit"])
        main(mock)
        captured = capfd.readouterr()
        assert "Quitting the app..." in captured.out

    def test_main_empty_command(self, capfd) -> None:
        mock = MockInputHandler(["quit","",""])
        main(mock)
        captured = capfd.readouterr()
        assert ">>\n>>\nQuitting the app..." in captured.out

    def test_main_Invalid_command(self, capfd) -> None:
        mock = MockInputHandler(["quit","","invalid"])
        main(mock)
        captured = capfd.readouterr()
        assert "Invalid Input!!!" in captured.out
