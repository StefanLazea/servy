import sys
import editor

from utils import get_argument, display_loading_message, hide_loading_message_with_error, write_error
from drive import get_worksheet, next_available_row, set_name_date


def write_command(user):
    if "-m" in sys.argv:
        try:
            description = None
            if "-t" in sys.argv:
                description = editor.edit()

            display_loading_message("Saving message", "Message saved")

            ws = get_worksheet()
            current_row = next_available_row(ws)
            set_name_date(current_row, user, ws)

            message = get_argument(sys.argv, "-m")
            ws.update_acell("C{}".format(current_row), message)

            if description:
                ws.update_acell("D{}".format(current_row), description.decode("utf-8"))

            hide_loading_message_with_error(False)
        except Exception:
            hide_loading_message_with_error(True)
    else:
        write_error("A message argument should be specified")
