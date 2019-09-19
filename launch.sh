#!/bin/bash

script_path=$(alias servy | grep -o -P '(?<=source ).*(?=/launch.sh)')
source "${script_path}/env/bin/activate"
user=$(whoami)
python3 py/command.py $EUID $user "$@"

deactivate