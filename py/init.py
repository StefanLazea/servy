import json
from utils import calculate_file_hash, display_loading_message, hide_loading_message_with_error, save_file_hash, validate_email
from drive import create_worksheet,  init_spreadsheet, get_worksheet

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

    shared_users = []
    while True:
        email = input("Insert email: ")
        if email:
            if validate_email(email):
                shared_users.append(email)
                print(shared_users)
            else:
                print("Invalid email. Insert another.")
        elif len(shared_users) == 0:
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
        create_worksheet(shared_users)
        init_spreadsheet()
        hide_loading_message_with_error(False)
    except Exception as e:
        hide_loading_message_with_error(True)
        print(e)


def main():
    init_app()


if __name__ == '__main__':
    main()
