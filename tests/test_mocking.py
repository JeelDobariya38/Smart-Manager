from SmartManager.App.controller import Controller
from SmartManager.App.command import Command, CommandInterface
from SmartManager.App.datahandler import Datahandler
from SmartManager.App.interface import CLI

import pytest

@pytest.fixture
def controller():
    controller = Controller()
    controller.userinterface = CLI()
    controller.command = Command()
    controller.datahandler = Datahandler()
    return controller

def test_controller(controller):
    assert isinstance(controller.command, CommandInterface)
    assert isinstance(controller.userinterface, CLI)
    assert isinstance(controller.datahandler, Datahandler)