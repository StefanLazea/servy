import json
from os import path
from init import init_app
from utils import calculate_file_hash


def try_init(message):
    print(message)
    if input("Do you want to init the app now? Y/N \n") == "Y":
        init_app()
    else:
        print("servy was not initialized. closing now.")
        exit(1)


def get_stored_hash():
    try:
        with open(path.abspath(path.join(__file__, "../../.servy"))) as hash_file:
            return hash_file.read()
    except FileNotFoundError:
        raise ReferenceError


def main():
    try:
        with open("storage.json", "r") as storage:
            if calculate_file_hash("storage.json") != get_stored_hash():
                raise ValueError

            storage_json = json.load(storage)
            if not storage_json['ss_name'] or not storage_json['shared_users'] or not storage_json['columns']:
                pass
    except FileNotFoundError:
        try_init("storage.json does not exist")
    except KeyError:
        try_init("storage.json is malformed")
    except ValueError:
        try_init("storage.json was altered after app init")
    except ReferenceError:
        try_init(".servy config file is missing")

    try:
        with open("credentials.json") as credentials:
            credentials_json = json.load(credentials)
            if not credentials_json['type'] or not credentials_json["project_id"] or not credentials_json["token_uri"] \
                    or not credentials_json['private_key_id'] or not credentials_json["private_key"] \
                    or not credentials_json['client_email'] or not credentials_json["auth_uri"] \
                    or not credentials_json['client_x509_cert_url'] or not credentials_json["auth_provider_x509_cert_url"]:
                pass
    except FileNotFoundError:
        print("credentials.json is missing. follow the docs to obtain one")
    except KeyError:
        print("credentials.json is malformed. ovewrite the current file")


if __name__ == '__main__':
    main()
