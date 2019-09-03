import sys
from utils import get_argument

if "-m" in sys.argv:
    print("Saving message: " + get_argument(sys.argv, "-m"))
