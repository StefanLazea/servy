import sys
from init import init_app
from help import help_command
from write import write_command
from read import read_command
from share import share_command
from version import version_command
from change import change_command
from delete import delete_command
from utils import hide_loading_message_with_error
from startup_check import startup_check


def switch(command, user, is_sudo):
    try:
        if command == "init":
            init_app()
        elif command == "write":
            startup_check()
            write_command(user)
        elif command == "read":
            startup_check()
            read_command()
        elif command == "share":
            startup_check()
            share_command()
        elif command == "change":
            startup_check()
            change_command(user)
        elif command == "version":
            version_command()
        elif command == "help":
            help_command()
        elif command == "delete":
            startup_check()
            delete_command(user, is_sudo)
    except KeyboardInterrupt:
        hide_loading_message_with_error(True, "\n")


if __name__ == "__main__":
    is_sudo = sys.argv[1]
    user = sys.argv[2]
    if len(sys.argv) >= 4:
        command = sys.argv[3]
        switch(command, user, is_sudo)
    else: 
        print("Please type a command. For further informations use `servy help`.")
