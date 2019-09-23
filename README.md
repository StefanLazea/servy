# **servy**
#### *your ultimate action tracking app*
*servy is a CLI app written in python that helps a team to keep a clean history of its actions without leaving the terminal*
###### servy uses Google Sheets to store the processed information

## Available packaging
### 1. [![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-white.svg)](https://snapcraft.io/servy)
### 2. Manual Installation
1. clone this repo
2. run "source ./install.sh"
    * In case you want `servy` alias to be available for every user in your system, run:
        ```sudo echo "alias servy='source $(pwd)/launch.sh'" >> /etc/bash.bashrc```
3. run "servy version" to check if the installation succeeded
4. [create a Google Cloud Platform project and download the generated credentials json](https://gspread.readthedocs.io/en/latest/oauth2.html) - *follow only the first 3 steps*
5. run "servy init" and follow the prompts
6. run "servy help" to check the available commands
7. **???**
8. profit
