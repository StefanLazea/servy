import sys
from utils import get_argument, display_loading_message, hide_loading_message_with_error, write_error
from drive import get_users_last_row, get_worksheet, delete_row


def delete_command(user, is_sudo):
    ws = get_worksheet()

    if "-r" in sys.argv:
        row = int(get_argument(sys.argv, "-r"))
        if row >= 2:
            try:
                display_loading_message("Deleting message", "Message deleted")

                if int(is_sudo) != 0:
                    selected_row = ws.row_values(row)
                    if selected_row[0] and user != selected_row[0]:
                        hide_loading_message_with_error(
                            True, "You cannot delete rows written by other users")
                        exit()

                delete_row(ws, row)
                hide_loading_message_with_error(False)
            except Exception as e:
                hide_loading_message_with_error(True, str(e))
        else:
            write_error("Invalid row")
    else:
        try:
            display_loading_message("Deleting message", "Message deleted")
            last_row = get_users_last_row(ws, user)
            delete_row(ws, last_row)
            hide_loading_message_with_error(False)
        except IndexError:
            hide_loading_message_with_error(
                True, "Error. No rows inserted by the current user")
