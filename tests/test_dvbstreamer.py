from dvbctrl.dvbstreamer import DVBStreamer


def test_dvbstreamer_loadclass():
    dvb = DVBStreamer(0)
    assert dvb.isRunning() == False


def test_dvbstreamer_start():
    dvb = DVBStreamer(0)
    dvb.start()
    assert dvb.isRunning() == True
    dvb.stop()
    assert dvb.isRunning() == False
