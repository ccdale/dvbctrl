import os
import time

from dvbctrl.commands import DVBCommand


def test_lslcn(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    chans = dvbc.lslcn()
    assert True == isinstance(chans, list)
    assert chans[0]["1"] == "BBC ONE East E"
    dvbc.close()


def test_lsmfs_nofilters(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.lsmfs()
    assert lines == []
    dvbc.close()


def test_lsservices_no_mux(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.lsservices()
    assert True == isinstance(lines, list)
    assert lines[0] == "BBC ONE East E"
    dvbc.close()


def test_lsservices_mux(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.lsservices(1653391414)
    assert True == isinstance(lines, list)
    assert lines[0] == "5STAR"
    dvbc.close()


def test_lsmuxes(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.lsmuxes()
    assert True == isinstance(lines, list)
    assert lines[0] == "1653391412"
    dvbc.close()


def test_lssfs(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.lssfs()
    assert True == isinstance(lines, list)
    assert lines[0] == "<Primary>"
    dvbc.close()


def test_lspids(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.lspids("5STAR")
    assert True == isinstance(lines, list)
    assert lines[0] == '4 PIDs for "5STAR"'
    dvbc.close()


def test_select(dvbobj):
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.select("BBC TWO")
    print(f"{lines=}")
    assert True == isinstance(lines, list)
    assert lines[0] == '233a.1047.10bf : "BBC TWO"'
    dvbc.close()


def test_setsf(dvbobj):
    svcfilt = "testsetsf"
    dvbc = DVBCommand()
    dvbc.open()
    op = dvbc.addsf(svcfilt)
    print(f"response from addsf {op=}")
    op = dvbc.getsf(svcfilt)
    print(f"response from getsf {op=}")
    op = dvbc.setsf(svcfilt, "BBC TWO")
    assert op == "OK"
    dvbc.rmsf(svcfilt)
    dvbc.close()


def test_set_get_mrl(dvbobj):
    # after 5 seconds the file should be greater than 1MB
    fn = "/tmp/test-bbc-two.ts"
    dvbc = DVBCommand()
    dvbc.open()
    lines = dvbc.select("BBC TWO")
    lines = dvbc.setmrl(f"file://{fn}")
    time.sleep(5)
    lines = dvbc.getmrl()
    assert True == isinstance(lines, list)
    assert lines[0] == f"file://{fn}"
    lines = dvbc.setmrl("null")
    dvbc.close()
    sz = os.stat(fn).st_size
    assert sz > 1024000
    os.unlink(fn)
