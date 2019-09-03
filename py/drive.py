import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)
gc = gspread.authorize(credentials)

try:
    sh = gc.open('History CLI')
    print("got it broah")
except:
    print("failed to retrieve ss: create new")
    sh = gc.create('History CLI')
    sh.share('bisagalexstefan@gmail.com', perm_type='user', role='writer')

worksheet = sh.sheet1
worksheet.update_cell(1, 1, "kisses from devops guys")
