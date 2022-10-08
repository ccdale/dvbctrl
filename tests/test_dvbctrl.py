import pytest
import sys
import time

from dvbctrl import __version__
from dvbctrl.commands import DVBCommand
from dvbctrl.connection import ControlConnection
from dvbctrl.dvbstreamer import DVBStreamer
from dvbctrl.errors import errorExit


@pytest.fixture(scope="module")
def dvbobj():
    try:
        dvb = DVBStreamer(0)
        running = dvb.start()
        if not running:
            raise Exception("Failed to start dvbstreamer on adaptor 0")
        yield dvb
        dvb.stop()
    except Exception as e:
        errorExit(sys.exc_info()[2], e)


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
    assert True == isinstance(lines, list)
    assert lines[0] == "BBC ONE East E"


def test_lsservices_mux(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    errmsg, lines = dvbc.lsservices(1653391414)
    assert errmsg == "OK"
    assert True == isinstance(lines, list)
    assert lines[0] == "5STAR"


def test_lsmuxes(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    errmsg, lines = dvbc.lsmuxes()
    assert errmsg == "OK"
    assert True == isinstance(lines, list)
    assert lines[0] == "1653391412"
