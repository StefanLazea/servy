from json import load, dump, decoder
from os import system
from reset import reset_command
from utils import display_loading_message, hide_loading_message_with_error, validate_email, print_permissions, write_error, get_credentials_path
from drive import create_spreadsheet, init_spreadsheet, get_worksheet, get_spreadsheet, delete_spreadsheet


def append_default_spreadsheet(credentials_path, default_spreadsheet):
    with open(credentials_path, "r+") as credentials:
        try:
            credentials_json = load(credentials)
            credentials_json["default_spreadsheet"] = default_spreadsheet
            credentials.seek(0, 0)
            dump(credentials_json, credentials)
            credentials.truncate()
        except decoder.JSONDecodeError:
            write_error("credentials.json does not contain a valid json")
            reset_command()
            exit()

def init_app():
    print("Starting servy init process")
    print("............................")
    credentials_path = get_credentials_path()
    while True:
        default_spreadsheet = input("Insert the spreadsheets name\n")
        if default_spreadsheet:
            try:
                append_default_spreadsheet(credentials_path, default_spreadsheet)
                break
            except FileNotFoundError:
                write_error("\n'credentials.json' does not exists")
                print("Copy the json from the downloaded file in the following input")
                input("Press any key to continue\n")
                open(credentials_path, "wb").close()
                try:
                    write_credentials = "nano " + credentials_path
                    system(write_credentials)
                    append_default_spreadsheet(credentials_path, default_spreadsheet)
                    break
                except Exception :
                    write_error("An error occured while saving credentials\n")
                    reset_command()
                    exit()
                    
    ss = get_spreadsheet()
    if ss and ss.sheet1:
        resume_ss = input(
            "A spreadsheet with this name already exists. Do you want to use it? Y/N\n")
        if resume_ss == "Y":
            print("Spreadsheet in use: " + default_spreadsheet)
            print("The following users has read permission to this file")
            print_permissions(ss)
            return

    print("Insert the email you want to have access to the spreadsheet")
    while True:
        email = input("Insert email: ")
        if email:
            if not validate_email(email):
                write_error("Invalid email")
            else:
                break

    display_loading_message("Creating spreadsheet " + default_spreadsheet, "Created spreadsheet " + default_spreadsheet)
    try:
        if ss:
            delete_spreadsheet(ss)
        ws = create_spreadsheet(email)
        init_spreadsheet(ws)
        hide_loading_message_with_error(False)
    except:
        hide_loading_message_with_error(True)
