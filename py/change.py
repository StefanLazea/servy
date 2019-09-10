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


def cell_update(worksheet, row, column, info):
    worksheet.update_cell(row, column, info)


previous_row = int(next_available_row(ws)) - 1
if "-m" in sys.argv:

    if "-r" in sys.argv:
        row_number = int(get_argument(sys.argv, "-r"))
        if row_number and row_number >= 1:
            try:
                row_update(row_number)
                hide_loading_message_with_error(False)
            except:
                hide_loading_message_with_error(True)
        else:
            print("Invalid number for -r option")
    else:
        row_update(previous_row)

    try:
        if "-d" in sys.argv:
            update_date(previous_row, 2)
        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)

    # try:
    #     if "-d" in sys.argv:
    #         update_date(previous_row, 2)
    #     hide_loading_message_with_error(False)
    # except:
    #     hide_loading_message_with_error(True)

else:
    print("A message argument should be specified")
