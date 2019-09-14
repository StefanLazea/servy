import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import get_spreadsheet_name, get_date


def create_spreadsheet(shared_user):
    gc = gspread.authorize(get_credentials())
    sh = gc.create(get_spreadsheet_name())
    share_spreadsheet(sh, shared_user)
    return sh.sheet1


def init_spreadsheet(ws):
    ws.update_title(get_spreadsheet_name())
    ws.update_cell(1, 1, "User")
    ws.update_cell(1, 2, "Date")
    ws.update_cell(1, 3, "Message")
    ws.update_cell(1, 4, "Details")


def get_credentials():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope)
    return credentials


def get_spreadsheet():
    gc = gspread.authorize(get_credentials())
    try:
        sh = gc.open(get_spreadsheet_name())
        return sh
    except:
        pass


def get_worksheet():
    sh = get_spreadsheet()
    return sh.sheet1


def next_available_row(ws):
    str_list = list(filter(None, ws.col_values(1)))
    return str(len(str_list) + 1)


def get_users_last_row(ws, user):
    rows = ws.findall(user)
    if rows:
        last_row = rows[-1].row
        return last_row
    else:
        raise IndexError


def get_last_n_rows(ws, number):
    last_row = int(next_available_row(ws)) - 1

    if number == -1:
        starting_row = 2
    else:
        starting_row = last_row - (number - 1) if last_row > number + 1 else 2

    rows = ws.range("A" + str(starting_row) + ":D" + str(last_row))
    rows.reverse()
    index = 0

    data_rows = []
    while index < len(rows):
        row = {}
        row["row"] = str(last_row)
        row["user"] = rows[index + 3].value
        row["date"] = rows[index + 2].value
        row["message"] = rows[index + 1].value
        row["details"] = rows[index].value
        data_rows.append(row)
        index = index + 4
        last_row = last_row - 1

    return data_rows


def share_spreadsheet(sh, email):
    sh.share(email, perm_type="user", role="reader")


def set_name_date(row, user, ws):
    ws.update_acell("A{}".format(row), user)
    ws.update_acell("B{}".format(row), get_date())


def update_cell(ws, row, column, info):
    ws.update_cell(row, column, info)


def update_row(ws, stored_row, row_number):
    cell_list = ws.range("A" + str(row_number) + ":D" + str(row_number))
    for i, val in enumerate(stored_row):
        cell_list[i].value = val
    ws.update_cells(cell_list)


def delete_spreadsheet(ss):
    gc = gspread.authorize(get_credentials())
    gc.del_spreadsheet(ss.id)


def delete_row(ws, row):
    ws.delete_row(row)
