import sys

from dvbctrl.colours import colours


def errorNotify(exci, e):
    lineno = exci.tb_lineno
    fname = exci.tb_frame.f_code.co_name
    ename = type(e).__name__
    msg = f"{colours.fg.red}{ename} Exception at line {lineno} in function {fname}: {e}{colours.reset}"
    # log.error(msg)
    print(msg)


def errorRaise(exci, e):
    errorNotify(exci, e)
    raise


def errorExit(exci, e):
    errorNotify(exci, e)
    sys.exit(1)
