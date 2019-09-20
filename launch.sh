#!/bin/bash
script_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
user=$(whoami)

source "${script_path}/env/bin/activate"
python3 "${script_path}/py/servy.py" $EUID $user "$@"
deactivate