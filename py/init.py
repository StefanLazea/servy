import re
import json
from utils import calculate_file_hash, display_loading_message, hide_loading_message_with_error
from drive import create_worksheet,  init_spreadsheet, get_worksheet


def validate_email(email):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(email_regex, email)):
        return True
    return False


def save_file_hash():
    hash = calculate_file_hash("storage.json")

    with open(".servy", "w+") as cfg:
        cfg.write(hash)


def init_app():
    print("Starting servy init process")
    print("............................")
    storage = {}
    while True:
        storage['ss_name'] = input("Insert the spreadsheets name\n")
        if storage['ss_name']:
            break

    print("Insert the email of the people you want to have access to the spreadsheet")
    print("When you want to finish, commit an empty input")

    storage['shared_users'] = []
    while True:
        email = input("Insert email: ")
        if email:
            if validate_email(email):
                storage['shared_users'].append(email)
            else:
                print("Invalid email. Insert another.")
        elif len(storage['shared_users']) == 0:
            print("At least one email is required")
        else:
            break

    with open('storage.json', 'w+') as storage_file:
        json.dump(storage, storage_file)

    save_file_hash()

    ss = get_worksheet()
    if ss:
        resume_ss = input("A spreadsheet with this name already exists. Do you want to use it?Y/N\n")
        if(resume_ss == "Y"):
            print("Skipped spreadsheet initialization")
            return

    display_loading_message(
        "Creating worksheet " + storage['ss_name'], "Created worksheet " + storage['ss_name'])

    try:
        create_worksheet()
        init_spreadsheet()
        hide_loading_message_with_error(False)
    except Exception as e:
        hide_loading_message_with_error(True)
        print(e)


def main():
    init_app()


if __name__ == '__main__':
    main()
