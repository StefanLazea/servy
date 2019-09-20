import sys
import datetime
from json import load
from time import sleep
from re import search
from threading import Thread
from os import path, environ
from colorama import Fore, Style


loaded = True
error = False
errorMessage = ""


def get_spreadsheet_name():
    with open(get_credentials_path(), "rb") as credentials:
        credentials_json = load(credentials)
        return credentials_json["default_spreadsheet"]


def get_credentials_path():
    try:
        return environ["SNAP_DATA"] + "credentials.json"
    except KeyError:
        return path.realpath(__file__).split("/py")[0] + "/credentials.json"


def get_argument(args, value):
    try:
        next_val = args[args.index(value) + 1]
    except:
        next_val = None

    if(not next_val or "-" in next_val):
        write_error("Argument not valid after " + value)
        exit()

    return next_val


def get_date():
    return str(datetime.datetime.now())


def print_permissions(ss):
    permissions = ss.list_permissions()
    for user in permissions:
        print(user["emailAddress"])


def write_error(message):
    print(Fore.RED + message + Style.RESET_ALL)


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


def display_loading_message(loading_message, finish_message):
    global loaded
    loaded = False
    thread = Thread(target=animate_loading,
                    args=(loading_message, finish_message,))
    thread.start()


def animate_loading(loading_message, finish_message):
    ss_loading = loading_message
    while not loaded:
        sys.stdout.write("\r" + ss_loading)
        sys.stdout.flush()
        ss_loading = ss_loading + "."
        sleep(0.2)
    if error is False:
        sys.stdout.write("\r" + finish_message + "\033[K\n")
    else:
        sys.stdout.write("\r" + errorMessage + "\033[K\n")


def hide_loading_message_with_error(withError, withMessage="An error occured"):
    global loaded, error, errorMessage
    loaded = True
    error = withError
    errorMessage = withMessage


def validate_email(email):
    email_regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if(search(email_regex, email)):
        return True
    return False
