#!/bin/bash

source env/bin/activate
cmd=$1;

user=$(whoami)
case $cmd in
    "write")
        python py/startup_check.py
        python py/write.py $@ $user
        ;;
    "version")
        python py/version.py
        ;;
    "help")
        echo "Halp pls"
        ;;
    "init")
        python py/init.py
        ;;
    *)
        echo "Command not known"
        ;;
esac