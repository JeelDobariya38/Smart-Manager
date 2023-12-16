from mocking import MockController


def test_welcome_msg(SmartManger, capfd):
    SmartManger.welcome()
    out, _ = capfd.readouterr()
    assert "Welcome to Smart Manager Application" in out


def test_app_exist(SmartManger):
    SmartManger.init()
    SmartManger.main()
