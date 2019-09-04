# basically needs to question user for data
# such as: ss_name and shared emails
# also needs to calculate a hash and store it in a

import re
import json

def validate_email(email):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(email_regex, email)):
        return True
    return False


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
        email = input("")
        if email:
            if validate_email(email):
                storage['shared_users'].append(email)
            else:
                print("Invalid email. Insert another.")
        else:
            break
    
    with open('storage.json', 'w+') as storage_file:
        json.dump(storage, storage_file)

    # calculate hash
    # save it to a .servy file in .etc 

def main():
    init_app()


if __name__ == '__main__':
    main()
