# File: tests/test_controller.py
from test_mocking import controller

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
