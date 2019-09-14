import sys
from utils import validate_email, get_argument, print_permissions, display_loading_message, hide_loading_message_with_error, write_error
from drive import get_spreadsheet, share_spreadsheet


def share_command():
    if "-l" in sys.argv:
        ss = get_spreadsheet()
        print_permissions(ss)
    elif "-a" in sys.argv:
        email = get_argument(sys.argv, "-a")
        if validate_email(email):
            try:
                display_loading_message("Adding permission", "Permission added")
                ss = get_spreadsheet()
                share_spreadsheet(ss, email)
                hide_loading_message_with_error(False)
            except Exception:
                hide_loading_message_with_error(True)
        else:
            write_error("Invalid email: " + email)
    elif "-d" in sys.argv:
        email = get_argument(sys.argv, "-d")
        if validate_email(email):
            try:
                display_loading_message("Removing permission", "Permission removed")
                ss = get_spreadsheet()
                ss.remove_permissions(email)
                hide_loading_message_with_error(False)
            except Exception:
                hide_loading_message_with_error(True)
        else:
            write_error("Invalid email: " + email)
