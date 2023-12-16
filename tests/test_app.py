from SmartManager import App

def test_welcome_msg(capfd):
    App().welcome()
    out, _ = capfd.readouterr()
    assert "Welcome to Smart Manager Application" in out
