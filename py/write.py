import sys
from utils import get_argument
from drive import get_worksheet
from datetime import date

if "-m" in sys.argv:
    print("Saving message: " + get_argument(sys.argv, "-m"))
