import sys

from dvbctrl.dvbv5 import Recorder
from dvbctrl.errors import errorNotify, errorExit


def main():
    try:
        r = Recorder()
        title = "Port of Escape"
        channel = "TalkingPictures TV"
        start = 1654263674
        stop = 1654264274
        r.setProgram(channel, title, start, stop)
        r.zapRecord()
    except Exception as e:
        errorNotify(sys.exc_info()[2], e)


if __name__ == "__main__":
    main()
