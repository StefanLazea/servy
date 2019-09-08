#!/bin/bash

#checks if python3 and venv are installed
#if not, installs python3 and venv
if command -v python3 &>/dev/null; then
    echo Python 3 is installed!
else
    echo python3 is now installing...
    sudo apt-get install python3
fi

if dpkg -s python3-venv &> /dev/null; then
    echo Package python3-venv is installed!
else
    echo python3-venv is now installing...
    sudo apt-get install python3-venv  
fi

#creates the env directory
python3 -m venv env --clear

#activates the env
source env/bin/activate

#installs the dependencies from the "dependencies" file using pip
pip3 install -r dependencies 
pip freeze

#creates an alias for history to current_directory/./launch.sh as a static path
echo "alias servy='source $(pwd)/launch.sh'" >> /etc/bash.bashrc
source /etc/bash.bashrc

echo "Welcome to history-cli, $(whoami)!"