# File: tests/test_controller.py
from test_mocking import controller
from SmartManager.App.command import HelpCommand, InvalidCommand

def test_get_command_valid_input(controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'help')
    cmd = controller.get_command()
    assert isinstance(cmd, HelpCommand)

def test_get_command_invalid_input(controller, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'invalid')
    cmd = controller.get_command()
    assert isinstance(cmd, InvalidCommand)

def test_initial_state(controller):
    assert not controller.isrunning()

def test_run_and_quit(controller):
    controller.run()
    assert controller.isrunning()

    controller.quit()
    assert not controller.isrunning()

def test_welcome_execution(capsys, controller):
    controller.welcome()

    captured = capsys.readouterr()
    assert "Welcome To Smart Manager" in captured.out
