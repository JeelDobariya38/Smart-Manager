from main import init, main

def test_init(capfd):
    init()
    captured = capfd.readouterr()
    assert "Welcome to Smart Manager Application" in captured.out
