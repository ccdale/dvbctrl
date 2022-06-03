"""Control module for dvbv5-zap."""

import os
import sys


from dvbctrl.errors import errorNotify, errorExit
from dvbctrl.shell import shellCommand


def zapRecord(channel, adapter, outputfn, length):
    try:
        home = os.path.expanduser("~/")
        tzap = f"{home}/.tzap"
        chanfn = f"{tzap}/dvb_channel.conf"
        cmd = f"dvbv5-zap -c {chanfn} -a {adapter} -p -r"
        cmd += f" -o {outputfn} -t {length} {channel}"
        data, err = shellCommand(cmd)
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)
