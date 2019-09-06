import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from utils import get_spreadsheet_name, get_shared_users


def get_credentials():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'credentials.json', scope)
    return credentials


def get_worksheet():
    gc = gspread.authorize(get_credentials())

    try:
        sh = gc.open(get_spreadsheet_name())
        return sh.sheet1
    except:
        print("failed to retrieve ss: create new")
        create_worksheet()


def create_worksheet():
    gc = gspread.authorize(get_credentials())
    sh = gc.create(get_spreadsheet_name())
    sh.share(get_shared_users(), perm_type='user', role='writer')


def init_spreadsheet():
    try:
        with open("storage.json", "r") as storage:
            storage_json = json.load(storage)
            index = 1
            for column_name in storage_json['columns']:
                if index <= len(storage_json['columns']):
                    get_worksheet().update_cell(1, index, column_name)
    except FileNotFoundError:
        print("Something went wrong")


def next_available_row():
    str_list = list(filter(None, get_worksheet().col_values(1)))
    return str(len(str_list)+1)