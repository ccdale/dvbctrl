import pytest

from dvbctrl.dvbstreamer import DVBStreamer


@pytest.fixture
def dvbobj(scope="session"):
    dvb = DVBStreamer(0)
    dvb.start()
    yield dvb
    dvb.stop()


# def test_dvbstreamer_loadclass(dvbobj):
#     assert dvbobj.isRunning() == True
#
#
# def test_dvbstreamer_start():
#     dvb = DVBStreamer(0)
#     dvb.start()
#     assert dvb.isRunning() == True
#     dvb.stop()
#     assert dvb.isRunning() == False
