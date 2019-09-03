#!/bin/bash
cmd=$1;
source env/bin/activate

case $cmd in
    "write")
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