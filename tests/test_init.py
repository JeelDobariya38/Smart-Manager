import app

def test_init(capfd):
    app.init()
    captured = capfd.readouterr()
    assert "Welcome to Smart Manager Application" in captured.out
