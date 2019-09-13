import sys
from init import init_app
from help import help_command
from write import write_command
from read import read_command
from share import share_command
from version import version_command
from change import change_command
from delete import delete_command


def switch(arg):
    try:
        if command == "init":
            init_app()
        elif command == "write":
            write_command(user)
        elif command == "read":
            read_command()
        elif command == "share":
            share_command()
        elif command == "change":
            change_command(user)
        elif command == "version":
            version_command()
        elif command == "help":
            help_command()
        elif command == "delete":
            delete_command(user)

    except KeyboardInterrupt:
        print("\n")


user = sys.argv[1]
if __name__ == "__main__":
    command = sys.argv[2]
    switch(command)
