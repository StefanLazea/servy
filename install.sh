# extracts the os
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     os=linux;;
    Darwin*)    os=mac;;
esac

# checks if python3 is installed, otherwise installs it
if command -v python3 &>/dev/null; then
    echo Python 3 is installed!
else
    echo python3 is now installing...

    if [ "$os" = 'linux' ]; then
      sudo apt-get install python3
    elif [ "$os" = 'mac' ]; then
      if [ -f "`which brew`" ]; then
        sudo brew install python
      else
        echo "brew is not installed"
      fi
    fi
fi

# creates the env directory
python3 -m venv env --clear

# activates the env
source env/bin/activate

# installs the dependencies from the "dependencies" file using pip
pip3 install -r requirements.txt
pip3 freeze

# creates an alias for history to current_directory/./launch.sh as a static path
main_shell=${SHELL##*/}
profile_file="$HOME/.${main_shell}rc"

echo "alias servy='sh $(pwd)/launch.sh'" >> "$profile_file"

echo -e "\n\nWelcome to servy, $(whoami)!\n\n"

# open new shell to source the changes
exec $main_shell
