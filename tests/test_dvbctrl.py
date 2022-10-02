import pytest

from dvbctrl import __version__
from dvbctrl.commands import DVBCommand
from dvbctrl.connection import ControlConnection
from dvbctrl.dvbstreamer import DVBStreamer


@pytest.fixture
def dvbobj(scope="module"):
    dvb = DVBStreamer(0)
    dvb.start()
    yield dvb
    dvb.stop()


def test_version():
    assert __version__ == "0.2.5"


def test_connect(dvbobj):
    # dvb = DVBStreamer(0)
    # dvb.start()
    cc = ControlConnection(0)
    cc.open()
    assert cc.opened == True
    assert cc.welcomemsg == "Ready"


def test_lslcn(dvbobj):
    # dvb = DVBStreamer(0)
    # dvb.start()
    dvbc = DVBCommand()
    lines = dvbc.lslcn()
    assert lines == "hello"
    # dvb.stop()
