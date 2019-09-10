"""change - rewrites the last message of the current user
-r - rewrite the message with the specified row
-m - the new message (mandatory)
-d - changes the original date with the current one
"""

import sys
import gspread
from utils import get_argument, get_date, display_loading_message, hide_loading_message_with_error
from drive import get_worksheet, next_available_row
from startup_check import startup_check

startup_check()
ws = get_worksheet()


def update_date(row, column):
    display_loading_message("Updating date", "Date updated")
    ws.update_cell(row, column, get_date())


def row_update(row):
    display_loading_message("Updating message", "Message updated")
    message = get_argument(sys.argv, "-m")
    ws.update_cell(row, 3, message)


previous_row = int(next_available_row(ws)) - 1
check = 0
if "-r" in sys.argv:
    row_number = int(get_argument(sys.argv, "-r"))
    if row_number and ws.row_values(row_number) != []:
        try:
            if row_number == -1 and "-m" in sys.argv:
                row_update(previous_row)
                check = 1
            else:
                row_update(row_number)
            hide_loading_message_with_error(False)
        except:
            hide_loading_message_with_error(True)
    else:
        print("The row " + str(row_number) + " is empty")
elif "-m" in sys.argv and check == 0:
    try:
        row_update(previous_row)
        if "-d" in sys.argv:
            update_date(previous_row, 2)
        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)
else:
    print("A message argument should be specified")
