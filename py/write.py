import sys
from utils import get_argument, get_date
from drive import get_worksheet, next_available_row
from datetime import date

if "-m" in sys.argv:
    print("Saving message: " + get_argument(sys.argv, "-m"))
    current_row = next_available_row()
    get_worksheet().update_acell("A{}".format(current_row), sys.argv[4])