import sys

from dvbctrl.dvbv5 import Recorder
from dvbctrl.errors import errorNotify, errorExit


def main():
    try:
        r = Recorder()
        title = "The Seventh Survivor"
        channel = "TalkingPictures TV"
        start = 1654254192
        stop = 1654255392
        r.setProgram(channel, title, start, stop)
        r.zapRecord()
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


if __name__ == "__main__":
    main()
