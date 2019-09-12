import sys
from utils import get_argument, display_loading_message, hide_loading_message_with_error
from drive import get_worksheet, next_available_row, set_name_date
from startup_check import startup_check

startup_check()
user = sys.argv[1]

if "-m" in sys.argv:
    try:
        ws = get_worksheet()
        current_row = next_available_row(ws)
        display_loading_message("Saving message", "Message saved")
        message = get_argument(sys.argv, "-m")
        set_name_date(current_row, user, ws)
        ws.update_acell("C{}".format(current_row), message)

        if "-t" in sys.argv:
            description = get_argument(sys.argv, "-t")
            ws.update_acell("D{}".format(current_row), description)

        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)
else:
    print("A message argument should be specified")
