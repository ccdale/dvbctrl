import os
import sys
import time

from dvbctrl.commands import DVBCommand
from dvbctrl.errors import errorNotify


class Recorder:
    """DVBStreamer recording class."""

    def __init__(
        self, channel, fqfn, adapter=0, host=None, user="dvbctrl", passw="dvbctrl"
    ):
        """Initialise the Recorder class."""
        try:
            self.channel = channel
            self.fqfn = fqfn
            self.dvbc = DVBCommand(adapter=adapter, host=host, user=user, passw=passw)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def _open(self):
        try:
            if not self.dvbc.opened:
                self.dvbc.open()
                if not self.dvbc.opened:
                    raise Exception(
                        f"Failed to open dvbctrl on adapter {self.dvbc.adapter}"
                    )
            return True
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def _close(self):
        try:
            self.dvbc.close()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def start(self):
        try:
            if not self._open():
                raise Exception(
                    f"Failed to open dvbctrl on adapter {self.dvbc.adapter}"
                )
            if self.dvbc.tuneToChannel(self.channel):
                self.dvbc.setmrl(f"file://{self.fqfn}")
                time.sleep(10)
                growing, sz = self.check(0)
                if not growing:
                    self.dvbc.setmrl("null://")
                    raise Exception(
                        f"Failed to start recording of {self.channel} to {self.fqfn}"
                    )
                return True
            return False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
        finally:
            self._close()

    def stop(self):
        try:
            if not self._open():
                raise Exception(
                    f"Failed to open dvbctrl on adapter {self.dvbc.adapter}"
                )
            return self.dvbc.setmrl("null://")
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
        finally:
            self._close()

    def check(self, lastsize):
        try:
            if os.path.isfile(self.fqfn):
                sz = os.path.getsize(self.fqfn)
                if sz > lastsize:
                    return (True, sz)
            return (False, lastsize)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
