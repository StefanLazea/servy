# **servy**
#### *your ultimate action tracking app*
*servy is a CLI app written in python & bash that helps a team to keep a clean history of its actions without leaving the terminal*
###### servy uses Google Sheets to store the processed information

## Installation
1. clone this repo
2. run "source ./install.sh"
    In case you want `servy` alias to be available for every user, run:
        ```sudo echo "alias servy='source $(pwd)/launch.sh'" >> /etc/bash.bashrc```
3. run "servy version" to check if the installation succeeded
4. [create a Google Cloud Platform project and download the generated credentials json](https://gspread.readthedocs.io/en/latest/oauth2.html) - *follow only the first 3 steps*
5. rename the json to credentials.json and move it to servy's folder
6. run "servy init" and follow the prompts
7. run "servy help" to check the available commands
8. **???**
9. profit