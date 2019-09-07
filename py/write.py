import sys
from utils import get_argument, get_date
from drive import get_worksheet, next_available_row, set_name_date

ws = get_worksheet()
user =  sys.argv[1]
current_row = next_available_row()
if "-m" in sys.argv:
    message =  get_argument(sys.argv, "-m")
    print("Saving message: " + message)
    set_name_date(current_row, user, ws)
    ws.update_acell("C{}".format(current_row), message)
elif "-t" in sys.argv:
    description =  get_argument(sys.argv, "-t")
    print("Saving description: " + description)
    ws.update_acell("D{}".format(int(current_row) - 1), description)
 