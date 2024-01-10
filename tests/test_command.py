# File: tests/test_command.py
from test_mocking import controller
from SmartManager.App.command import Command, HelpCommand, QuitCommand, InvalidCommand

def test_empty_command(controller):
    assert not controller.command.match("")

def test_add_command():
    Command.add(HelpCommand())
    assert isinstance(Command.commands[-1], HelpCommand)

def test_help_command_execution(capsys, controller):
    command = HelpCommand()
    
    command.execute(controller)

    captured = capsys.readouterr()
    assert "Here is list of valid Commands:\n\n" in captured.out
    assert "Commands:\n" in captured.out

def test_invalid_command_execution(capsys, controller):
    command = InvalidCommand()

    command.execute(controller)

    captured = capsys.readouterr()
    assert "Invalid Command!!" in captured.out
