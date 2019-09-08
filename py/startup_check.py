import json
from os import path
from init import init_app


def try_init(message):
    print(message)
    if input("Do you want to init the app now? Y/N \n") == "Y":
        init_app()
    else:
        exit()


def startup_check():
    try:
        with open("credentials.json") as credentials:
            credentials_json = json.load(credentials)
            if not credentials_json['type'] or not credentials_json["project_id"] or not credentials_json["token_uri"] \
                    or not credentials_json['private_key_id'] or not credentials_json["private_key"] \
                    or not credentials_json['client_email'] or not credentials_json["auth_uri"] \
                    or not credentials_json['client_x509_cert_url'] or not credentials_json["auth_provider_x509_cert_url"] \
                    or not credentials_json['default_spreadsheet']:
                pass
    except FileNotFoundError:
        try_init("credentials.json is missing.")
    except KeyError:
        try_init("credentials.json is malformed.")
