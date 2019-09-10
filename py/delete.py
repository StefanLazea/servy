import sys
from startup_check import startup_check
from utils import get_argument, display_loading_message, hide_loading_message_with_error
from drive import get_users_last_row, get_worksheet, delete_row

startup_check()

ws = get_worksheet()
user = sys.argv[1]

if "-r" in sys.argv:
    row = int(get_argument(sys.argv, "-r"))
    if row >= 2:
        try:
            display_loading_message("Deleting message", "Message deleted")
            delete_row(ws, row)
            hide_loading_message_with_error(False)
        except:
            hide_loading_message_with_error(True)
    else:
        print("Invalid row")
else:
    try:
        display_loading_message("Deleting message", "Message deleted")
        last_row = get_users_last_row(ws, user)
        delete_row(ws, last_row)
        hide_loading_message_with_error(False)
    except IndexError:
        hide_loading_message_with_error(True, "Error. No rows inserted by the current user")
