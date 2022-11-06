import os

from dvbctrl.recorder import Recorder


def test_recorder(dvbobj):
    fn = "/tmp/test_recorder_bbc_two.ts"
    r = Recorder("BBC TWO", fn, adapter=dvbobj.adapter)
    running = r.start()
    assert running == True
    running, sz = r.check(0)
    assert running == True
    assert sz > 0
    running = r.stop()
    assert running[0] == 'MRL set to "null://" for <Primary>'
    os.unlink(fn)
