#!/bin/bash

script_path=$(alias servy | grep -o -P '(?<=source ).*(?=/launch.sh)')
source "${script_path}/env/bin/activate"
cmd=$1;

user=$(whoami)
case $cmd in
    "init")
        python py/init.py
        ;;
    "write")
        python py/write.py $user "$@"
        ;;
    "read")
        python py/read.py $user "$@"
        ;;
    "share")
        python py/share.py "$@"
        ;;
    "change")
        python py/change.py "$@"
        ;;
    "version")
        python py/version.py
        ;;
    "help")
        python py/help.py
        ;;
    *)
        echo "servy - Command not known. Use 'servy help' for available commands!"
        ;;
esac
deactivate