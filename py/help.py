"""    servy - your ultimate action tracking app

Commands:

    servy init                            Inits the app

    servy share [options] | <email>       Performs operations on the spreadsheets user permission   
        Options:
            -l           Get spreadsheet and prints permissions
            -a <email>   Add a new user to the spreadsheet
            -d <email>   Delete an user

    servy write [options] | <text>        Stores messages in the current worksheet
        Options:
            -m <message>    Writes a short message describing the action made - Required!
            -t <text>       Adds a longer description of what was done

    servy read [options]                  Prints the last 10 rows
        Options:
            -a              Returns all rows from the spreadsheet
            -n <number>     Given the <number> argument, it will return the exact number of rows

    servy change [options] | <text>       Updates the information saved on a row
        Options
            -m <message>   Changes the message of the last row inserted by the current user - Required!
            -t <text>      Changes the details of the last row inserted by the current user
            -d             Updates the date of the last row inserted by the current user to present
            -r <number>    Apply the changes to the specified row instead of the last one

    servy delete [options]                Removes the last row inserted by the current user
        Options
            -r <number>    Removes the specified row if it was inserted by the current user
                           If the command is run using sudo, it can remove any row
    
    servy reset                           Resets servy by removing credentials.json

    servy version                         Displays the version

    servy help                            You're looking at it rn
"""


def help_command():
    print(__doc__)
