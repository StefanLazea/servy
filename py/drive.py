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
