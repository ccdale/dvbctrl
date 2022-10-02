from dvbctrl.commands import DVBCommand
from dvbctrl.dvbstreamer import DVBStreamer


def test_lslcn():
    dvb = DVBStreamer(0)
    dvb.start()
    dvbc = DVBCommand()
    lines = dvbc.lslcn()
    assert lines == "hello"
    dvb.stop()
