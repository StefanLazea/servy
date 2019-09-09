
"""HISTORY CLI - servy

Usage:
    servy init          Inits the app.
    servy share [options] | <email>       Performs operations on the spreadsheets user permission.      
        Options:
            -l           Get spreadsheet and prints permissions.
            -a <email>   Add a new user to the spreadsheet.
            -d <email>   Delete an user.

    servy write [options] | <text>
        Options:
            [(-m <message>)]    Writes a short message describing the action made. Required!
            [(-t <text>)]       Adds a longer description of what was done.
    servy read          Prints the last 10 rows.
    servy version       Show version.
    servy help          You looking at it.
"""
print(__doc__)