#!/bin/bash
cmd=$1;

case $cmd in 
    "create")
        python3 py/create.py $@
        ;;
    "version")
        python3 py/version.py
        ;;
    "help")
        echo "Halp pls"
        ;;
    *)
        echo "Command not known"
        ;;
esac