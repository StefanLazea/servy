import sys
import pydoc
from drive import get_worksheet, get_last_n_rows
from utils import get_argument, format_log, write_error, display_loading_message, hide_loading_message_with_error


def read_command():
    try:
        display_loading_message("Loading messages", "")
        ws = get_worksheet()

        if "-a" in sys.argv:
            n = -1
        elif "-n" in sys.argv:
            n = int(get_argument(sys.argv, "-n"))
        else:
            n = 10

        rows = get_last_n_rows(ws, n)
        formatted_rows = format_log(rows)
        hide_loading_message_with_error(False)
        pydoc.pipepager(formatted_rows, cmd="less -R")
        print("")
    except Exception:
        raise KeyboardInterrupt
