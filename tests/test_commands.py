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
