import pytest
import time

from dvbctrl import __version__
from dvbctrl.commands import DVBCommand
from dvbctrl.connection import ControlConnection
from dvbctrl.dvbstreamer import DVBStreamer


@pytest.fixture(scope="module")
def dvbobj():
    dvb = DVBStreamer(0)
    dvb.start()
    # time.sleep(1)  # give it some time to settle
    yield dvb
    dvb.stop()


def test_version():
    assert __version__ == "0.2.6"


def test_isrunning(dvbobj):
    assert True == dvbobj.isRunning()


def test_connect(dvbobj):
    cc = ControlConnection(0)
    cc.open()
    assert cc.opened == True
    assert cc.welcomemsg == "Ready"


def test_lslcn(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    errmsg, lines = dvbc.lslcn()
    assert errmsg.strip().split()[1] == "channels"
    assert True == isinstance(lines, list)
    assert lines[0] == "   1 : BBC ONE East E"


def test_lsmfs_nofilters(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    errmsg, lines = dvbc.lsmfs()
    assert lines == []
    assert errmsg == "OK"

def test_lsservices_no_mux(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    errmsg, lines = dvbc.lsservices()
    assert errmsg == "OK"
    assert true isinstance(lines, list)
    assert lines[0] == "   1 : BBC ONE East E"
