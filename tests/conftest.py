import sys

import pytest

from dvbctrl.dvbstreamer import DVBStreamer
from dvbctrl.errors import errorExit


@pytest.fixture(scope="session")
def dvbobj():
    try:
        dvb = DVBStreamer(3)
        running = dvb.start()
        if not running:
            raise Exception("Failed to start dvbstreamer on adapter 3")
        yield dvb
        dvb.stop()
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
