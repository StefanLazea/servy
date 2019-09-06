import sys
import json
import time
import threading
from os import path
from datetime import date
import hashlib

loaded = True
error = False


def get_storage():
    storage = json.load(open("storage.json"))
    return storage


def get_spreadsheet_name():
    storage = get_storage()
    return storage['ss_name']


def get_shared_users():
    storage = get_storage()
    return storage['shared_users']


def calculate_file_hash(file_name):
    with open(file_name, "rb") as file:
        sha1 = hashlib.sha1()
        BUF_SIZE = 65536
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

        return sha1.hexdigest()


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
        print("\n" + finish_message)
    else:
        print("\n An error occured")


def hide_loading_message(withError):
    global loaded, error
    loaded = True
    error = withError

def get_date():
    return date.today()
