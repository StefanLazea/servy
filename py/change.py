import sys
from utils import get_argument, get_date, display_loading_message, hide_loading_message_with_error
from drive import get_worksheet, next_available_row, update_cell, get_users_last_row, update_row
from startup_check import startup_check
import gspread

startup_check()
ws = get_worksheet()

message_flag = 0
row_flag = 0
date_flag = 0
description_flag = 0

user = sys.argv[1]
stored_row = ws.row_values(get_users_last_row(ws, user))
message = ""
description = ""
row_number = -1


if "-m" in sys.argv:
    message_flag = 1
    message = get_argument(sys.argv, "-m")
    if "-r" in sys.argv:
        row_number = int(get_argument(sys.argv, "-r"))
        if row_number and row_number >= 2:
            selected_row = ws.row_values(row_number)
            if user == stored_row[0]:
                stored_row = selected_row
                row_flag = 1
            else:
                print("You can't edit others information")
    else:
        row_number = get_users_last_row(ws, user)
        stored_row = ws.row_values(row_number)

    if "-t" in sys.argv:
        description_flag = 1
        description = get_argument(sys.argv, "-t")

    if "-d" in sys.argv:
        date_flag = 1

if message_flag != 1:
    print("Please check the help section using 'servy help'")
else:
    try:
        display_loading_message("Updating info", "Information updated")

        if description_flag == 1:
            if date_flag == 1:
                stored_row = [stored_row[0], get_date(), message, description]
                update_row(ws, stored_row, row_number)
            else:
                stored_row = [stored_row[0], stored_row[1], message, description]
                update_row(ws, stored_row, row_number)
        else:
            if date_flag == 1:
                stored_row = [stored_row[0], get_date(), message, stored_row[3]]
                update_row(ws, stored_row, row_number)
            else:
                stored_row = [stored_row[0], stored_row[1], message, stored_row[3]]
                update_row(ws, stored_row, row_number)

        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)
