import sys
from utils import get_argument, get_date
from drive import get_worksheet, next_available_row, set_name_date

if "-m" in sys.argv:
    print("Saving message: " + get_argument(sys.argv, "-m"))
    user =  sys.argv[4]
    set_name_date(next_available_row(), user)
   