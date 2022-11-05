from dvbctrl import __version__
from dvbctrl.connection import ControlConnection


def test_version():
    assert __version__ == "0.3.7"


def test_isrunning(dvbobj):
    assert True == dvbobj.isRunning()


def test_connect(dvbobj):
    cc = ControlConnection(3)
    cc.open()
    assert cc.opened == True
    assert cc.welcomemsg == "Ready"
