import sys
import json
from utils import calculate_file_hash, get_storage, validate_email, save_file_hash, get_argument
from drive import get_spreadsheet, share_spreadsheet
from startup_check import startup_check

startup_check()

if "-l" in sys.argv:
    ss = get_spreadsheet()
    permissions = ss.list_permissions()
    for user in permissions:
        print(user['emailAddress'])
elif "-a" in sys.argv:
    email = get_argument(sys.argv, "-a")
    if validate_email(email):
        ss = get_spreadsheet()
        share_spreadsheet(ss, email)
    else:
        print("Invalid email: " + email)
elif "-d" in sys.argv:
    email = get_argument(sys.argv, "-d")
    if validate_email(email):
        ss = get_spreadsheet()
        ss.remove_permissions(email)
    else:
        print("Invalid email: " + email)
