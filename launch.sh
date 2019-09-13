#!/bin/bash

script_path=$(alias servy | grep -o -P '(?<=source ).*(?=/launch.sh)')
source "${script_path}/env/bin/activate"

cmd=$1;
user=$(whoami)
python py/command.py $EUID $user "$@"

deactivate