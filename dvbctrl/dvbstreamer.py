"""dvbstreamer commands."""
import os
from pathlib import Path
import sys

import psutil

from dvbctrl.errors import errorNotify
from dvbctrl.shell import shellCommand


def startDvbStreamer(cfg, adapter):
    try:
        cmd = "dvbstreamer -a {adapter} -d -D -u cfg['user'] -p cfg['password']"
        data, err = shellCommand(cmd)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


class DVBStreamer:
    def __init__(self, adapter):
        try:
            self.adapter = int(adapter)
            self.user = "dvbctrl"
            self.password = "dvbctrl"
            self.running = False
            self.setPidFile()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def __del__(self):
        """TODO connect to this instance and issue quit"""
        try:
            if self.isRunning():
                p = psutil.Process(self.pid)
                p.terminate()
                # wait 3 seconds for the process to end
                # if it is still alive after that, kill it with fire
                gone, alive = psutil.wait_procs([p], timeout=3)
                if len(alive) > 0:
                    p.kill()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def start(self):
        try:
            cmd = f"dvbstreamer -a {self.adapter} -d -D"
            cmd += f" -u {self.user} -p {self.password}"
            data, err = shellCommand(cmd)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def setPidFile(self):
        try:
            pidfn = f"dvbstreamer-{self.adapter}.pid"
            fqpidfn = os.path.expanduser(f"~/.dvbstreamer/{pidfn}")
            self.pidfn = Path(fqpidfn)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def getProcessadapter(self, pinfo):
        """Extracts the adapter number from the cmd line of the process."""
        try:
            # psutil.process.cmdline should return a list of strings
            # we are looking for the value after a '-a'
            padapter = None
            pcn = -1
            for cn, xstr in enumerate(pinfo["cmdline"]):
                if xstr == "-a":
                    pcn = cn + 1
                    break
            if pcn > 0:
                padapter = int(pinfo["cmdline"][pcn])
            return padapter
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def findMyProcessPid(self):
        try:
            mypid = None
            for p in psutil.process_iter(["pid", "name", "cmdline"]):
                if "dvbstreamer" in p.info["name"]:
                    padapter = getProcessadapter(p.info)
                    if padapter == self.adapter:
                        mypid = int(p.info["pid"])
            return mypid
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def isRunning(self):
        try:
            if self.pidfn.exists():
                with open(self.pidfn, "r") as ifn:
                    spid = ifn.readall()
                self.pid = int(spid)
            pmypid = findMyProcessPid()
            if pmypid and pmypid == self.pid:
                return True
            return False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)


class Control:
    def __init__(self, adapter):
        try:
            self.adapter = adapter
            self.user = "dvbctrl"
            self.password = "dvbctrl"
            self.connected = False
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def connect(self):
        try:
            # cmd =
            pass
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
