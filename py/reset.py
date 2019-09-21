from utils import get_credentials_path
from os import remove

def reset_command():
    credentials_path = get_credentials_path()
    try:
        remove(credentials_path)
        print("servy was resetted")
        print("run \"sudo servy init\" to reconfigure servy")
    except PermissionError:
        write_error("`servy reset` should be run with root permissions")
    except FileNotFoundError:
        print("servy is already resetted")