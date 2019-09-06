import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from utils import get_spreadsheet_name, get_shared_users, get_date


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
        recreate = input("Spreadsheet doesn't exist. Do you want to create it? Y/N \n")
        if recreate == "Y":
            create_worksheet()


def create_worksheet():
    gc = gspread.authorize(get_credentials())
    sh = gc.create(get_spreadsheet_name())
    sh.share(get_shared_users(), perm_type='user', role='writer')


def init_spreadsheet():
    ws = get_worksheet()
    ws.update_title(get_spreadsheet_name())
    ws.update_cell(1, 1, "Nr.")
    ws.update_cell(1, 2, "User")
    ws.update_cell(1, 3, "Date")
    ws.update_cell(1, 4, "Message")
    ws.update_cell(1, 5, "Details")


def next_available_row():
    str_list = list(filter(None, get_worksheet().col_values(1)))
    return str(len(str_list)+1)


def set_name_date(row, user, ws):
    ws.update_acell("A{}".format(row), user)
    ws.update_acell("C{}".format(row), get_date())


def main():
    create_worksheet()


if __name__ == '__main__':
    main()
