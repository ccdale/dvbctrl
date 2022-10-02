from dvbctrl.connection import ControlConnection
from dvbctrl.dvbstreamer import DVBStreamer


def test_connect():
    dvb = DVBStreamer(0)
    cc = ControlConnection(0)
    cc.open()
    assert cc.opened == True
    assert cc.welcomemsg == "Ready"
