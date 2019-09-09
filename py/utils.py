import sys
import json
import time
import re
import threading
from os import path
import datetime
import hashlib
from colorama import Fore, Style

loaded = True
error = False


def get_spreadsheet_name():
    with open("credentials.json", "rb") as credentials:
        credentials_json = json.load(credentials)
        return credentials_json["default_spreadsheet"]


def get_argument(args, value):
    try:
        next_val = args[args.index(value) + 1]
    except:
        next_val = None

    if(not next_val or "-" in next_val):
        print("Argument not valid after " + value)
        sys.exit()

    return next_val


def display_loading_message(loading_message, finish_message):
    global loaded
    loaded = False
    thread = threading.Thread(target=animate_loading,
                              args=(loading_message, finish_message,))
    thread.start()


def animate_loading(loading_message, finish_message):
    ss_loading = loading_message
    while not loaded:
        sys.stdout.write("\r" + ss_loading)
        sys.stdout.flush()
        ss_loading = ss_loading + "."
        time.sleep(0.2)

    if error is False:
        sys.stdout.write("\r" + finish_message + "\033[K\n")
    else:
        print("\n An error occured")


def hide_loading_message_with_error(withError):
    global loaded, error
    loaded = True
    error = withError


def get_date():
    return str(datetime.datetime.now())


def validate_email(email):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(email_regex, email)):
        return True
    return False


def print_permissions(ss):
    permissions = ss.list_permissions()
    for user in permissions:
        print(user['emailAddress'])


def format_log(logs):
    log_string = "\n"

    for log in logs:
        log_string += Fore.GREEN + "Message: " + log["message"] + "\n"
        log_string += Fore.YELLOW + "User: " + log["user"] + "\n"
        log_string += "Date: " + log["date"] + "\n"
        log_string += "Row:" + log["row"] + "\n"

        if log["details"]:
            log_string += "Details: " + "\n\t" + log["details"] + "\n"

        log_string += "\n"

    return log_string
