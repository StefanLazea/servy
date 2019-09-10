"""HISTORY CLI - servy
Your ultimate action tracking app.

Usage:
    servy init          Inits the app.
    servy share [options] | <email>       Performs operations on the spreadsheets user permission.      
        Options:
            -l           Get spreadsheet and prints permissions.
            -a <email>   Add a new user to the spreadsheet.
            -d <email>   Delete an user.

    servy write [options] | <text>
        Options:
            -m <message>    Writes a short message describing the action made. Required!
            -t <text>       Adds a longer description of what was done.

    servy read [options]    Prints the last 10 rows.
        Options:
            -a              Returns all rows from the spreadsheet.
            -n <number>     Given the <number> argument, it will return the exact number of rows.
    servy change [options] | <message> | [options]
    servy version       Show version.
    servy help          You looking at it.
"""
print(__doc__)