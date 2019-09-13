import sys
import pydoc
from startup_check import startup_check
from drive import get_worksheet, get_last_n_rows
from utils import get_argument, format_log

startup_check()


def read_command():
    ws = get_worksheet()

    if "-a" in sys.argv:
        n = -1
    elif "-n" in sys.argv:
        n = int(get_argument(sys.argv, "-n"))
    else:
        n = 10

    rows = get_last_n_rows(ws, n)
    formatted_rows = format_log(rows)
    pydoc.pipepager(formatted_rows, cmd='less -R')

