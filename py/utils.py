import sys


def get_argument(args, value):
    try:
        next_val = args[args.index(value) + 1]
    except:
        next_val = None

    if(not next_val or "-" in next_val):
        print("Argument not valid after " + value)
        sys.exit()

    return next_val
