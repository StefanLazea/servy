#!/bin/bash

source env/bin/activate
cmd=$1;

case $cmd in
    "write")
        python py/startup_check.py || exit
        python py/write.py $@
        ;;
    "version")
        python py/version.py
        ;;
    "help")
        echo "Halp pls"
        ;;
    *)
        echo "Command not known"
        ;;
esac