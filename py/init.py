import json
from utils import display_loading_message, hide_loading_message_with_error, validate_email, print_permissions
from drive import create_spreadsheet, init_spreadsheet, get_worksheet, get_spreadsheet, delete_spreadsheet


def init_app():
    print("Starting servy init process")
    print("............................")
    while True:
        default_spreadsheet = input("Insert the spreadsheets name\n")
        if default_spreadsheet:
            try:
                with open("credentials.json", "r+") as credentials:
                    credentials_json = json.load(credentials)
                    credentials_json["default_spreadsheet"] = default_spreadsheet
                    credentials.seek(0, 0)
                    json.dump(credentials_json, credentials)
                    credentials.truncate()
                break
            except FileNotFoundError:
                print("credentials.json doesn't exist. follow the instructions")
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
                print("Invalid email")
            else:
                break

    display_loading_message(
        "Creating spreadsheet " + default_spreadsheet, "Created spreadsheet " + default_spreadsheet)
    try:
        if ss:
            delete_spreadsheet(ss)
        ws = create_spreadsheet(email)
        init_spreadsheet(ws)
        hide_loading_message_with_error(False)
    except Exception as e:
        hide_loading_message_with_error(True)
        print(e)


if __name__ == '__main__':
    init_app()
