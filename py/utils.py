import sys
import json
from os import path
import hashlib


def get_storage():
    storage = json.load(open("storage.json"))
    return storage


def get_spreadsheet_name():
    storage = get_storage()
    return storage['ss_name']


def get_shared_users():
    storage = get_storage()
    return storage['shared_users']


def calculate_file_hash(file):
    sha1 = hashlib.sha1()
    BUF_SIZE = 65536
    while True:
        data = file.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)

    print(sha1.hexdigest())


def get_stored_hash():
    with open(path.abspath(path.join(__file__, "../../.servy"))) as hash_file:
        return hash_file.read()


def get_argument(args, value):
    try:
        next_val = args[args.index(value) + 1]
    except:
        next_val = None

    if(not next_val or "-" in next_val):
        print("Argument not valid after " + value)
        sys.exit()

    return next_val


def main():
    get_stored_hash()
    # calculate_file_hash("storage.json")


if __name__ == '__main__':
    main()
