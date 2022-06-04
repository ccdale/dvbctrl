"""Control module for dvbv5-zap."""

from datetime import datetime
import os
from pathlib import Path
import sys


from dvbctrl.errors import errorNotify
from dvbctrl.shell import shellCommand


class Recorder:
    def __init__(self, adapter=0, basefd=None):
        try:
            self.adapter = adapter
            self.basefd = (
                Path(basefd) if basefd else Path("/run/media/chris/seagate4/TV/tv")
            )
            self.basefd.mkdir(parents=True, exist_ok=True)
            self.fqfn = None
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def setProgram(self, channel, title, start, stop):
        try:
            self.channel = channel
            self.title = title
            self.start = start
            self.stop = stop
            self.length = int(stop - start)
            fchan = self.channel.replace(" ", "_")
            ftitle = self.title.replace(" ", "_")
            dt = datetime.fromtimestamp(start)
            fn = f"{dt.year}{dt.month:0>2}{dt.day:0>2}T{dt.hour:0>2}{dt.minute:0>2}"
            fn += f"-{fchan}-{ftitle}.ts"
            self.fdir = Path(self.basefd / ftitle)
            self.fdir.mkdir(parents=True, exist_ok=True)
            self.fqfn = Path(self.fdir / fn)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def zapRecord(self):
        try:
            if not self.fqfn:
                raise Exception("Current program not yet setup")
            print(f"starting a recording to {self.fqfn}")
            home = os.environ.get("HOME", os.path.expanduser("~/"))
            tzap = f"{home}/.tzap"
            chanfn = f"{tzap}/dvb_channel.conf"
            scmd = f"dvbv5-zap -c {chanfn} -a {self.adapter} -p -r"
            scmd += f" -o {self.fqfn} -t {self.length}"
            cmd = scmd.split()
            cmd.append(self.channel)
            print(f"{cmd=}")
            data, err = shellCommand(cmd)
            print(f"{data=}\n{err=}")
            print(f"recording to {self.fqfn} completed")
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
