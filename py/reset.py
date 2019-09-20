from utils import get_credentials_path
from os import remove

def reset_command():
    credentials_path = get_credentials_path()
    remove(credentials_path)
    print("servy was resetted")
    print("run \"servy init\" to reconfigure servy")