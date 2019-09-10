"""change - rewrites the last message of the current user
-r - rewrite the message with the specified row
-m - the new message (mandatory)
-d - changes the original date with the current one
"""

import sys
import gspread
from utils import get_argument, get_date, display_loading_message, hide_loading_message_with_error
from drive import get_worksheet, next_available_row, cell_update
from startup_check import startup_check

startup_check()
ws = get_worksheet()


if "-m" in sys.argv:
    previous_row = int(next_available_row(ws)) - 1
    message = get_argument(sys.argv, "-m")
    check = 0
    row_number = 0
    if "-r" in sys.argv:
        row_number = int(get_argument(sys.argv, "-r"))
        if row_number and row_number >= 1:
            try:
                display_loading_message("Updating message", "Message updated")
                cell_update(ws, row_number, 3, message)
                check = 1
                hide_loading_message_with_error(False)
            except:
                hide_loading_message_with_error(True)
        else:
            print("Invalid number for -r option")
    else:
        display_loading_message("Updating message", "Message updated")
        cell_update(ws, previous_row, 3, message)

    try:
        if "-d" in sys.argv:
            display_loading_message("Updating date", "Date updated")
            if check == 1:
                cell_update(ws, row_number, 2, get_date())
                pass
            cell_update(ws, previous_row, 2, get_date())
        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)

    try:
        if "-t" in sys.argv:
            display_loading_message("Updating description", "Description updated")

            description = get_argument(sys.argv, "-t")
            cell_update(ws,previous_row, 4, description)
        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)

else:
    print("A message argument should be specified")
