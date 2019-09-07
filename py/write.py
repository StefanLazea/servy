import sys
from utils import get_argument, get_date
from drive import get_worksheet, next_available_row, set_name_date
from startup_check import startup_check

startup_check()

if "-m" in sys.argv:
    print("Saving message: " + get_argument(sys.argv, "-m"))
    user =  sys.argv[4]
    ws = get_worksheet()
    set_name_date(next_available_row(), user, ws)
   