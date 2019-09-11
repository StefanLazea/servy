import sys
import gspread
from utils import get_argument, get_date, display_loading_message, hide_loading_message_with_error, write_error
from drive import get_worksheet, next_available_row, update_cell, get_users_last_row, update_row
from startup_check import startup_check

startup_check()

ws = get_worksheet()
user = sys.argv[1]

try:
    if "-r" in sys.argv:
        row_number = int(get_argument(sys.argv, "-r"))
        if row_number and row_number >= 2:
            selected_row = ws.row_values(row_number)
            if user == selected_row[0]:
                stored_row = selected_row
            else:
                write_error("You can't edit others information")
                exit()
        else:
            write_error("Invalid row")
            exit()
    else:
        row_number = get_users_last_row(ws, user)
        stored_row = ws.row_values(row_number)

    display_loading_message("Updating info", "Information updated")

    new_date = get_date() if "-d" in sys.argv else stored_row[1]
    new_message = get_argument(sys.argv, "-m") if "-m" in sys.argv else stored_row[2]
    new_description = get_argument(sys.argv, "-t") if "-t" in sys.argv else stored_row[3]

    stored_row = [stored_row[0], new_date, new_message, new_description]
    update_row(ws, stored_row, row_number)

    hide_loading_message_with_error(False)
except:
    hide_loading_message_with_error(True)
