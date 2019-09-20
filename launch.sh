#!/bin/bash
script_path=$(alias servy | grep -o -P '(?<=source ).*(?=/launch.sh)')
user=$(whoami)

source "${script_path}/env/bin/activate"
python3 py/servy.py $EUID $user "$@"
deactivate