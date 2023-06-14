
# Css Cleanup Helper - Uses Django Framework
This tool allows you to scrape the current contents of a site and detect where links are used, css classes, and html elements.

## How to use
1. Download the repository
2. Install requirements.txt (`python3 -m pip install -r ./requirements.txt`)
3. Migrate the database (`python3 manage.py makemigrations && python3 manage.py migrate`)
4. Make a .env file in the settings folder with the following text
```
    SECRET_KEY=anything_good_here
```
5. Install the [Webdrive for Edge](https://selenium-python.readthedocs.io/installation.html)
6. Run the commands in the Commands section

## Commands -
### Convert website into database entries (IF YOU DONT HAVE DATABASE)

`python manage.py scrape --base-url https://education.byu.edu`  
  
`--base-url` (required): The base where you would like the scrapper to start.

### Search for css stylesheets that are unused (IF YOU DONT HAVE DATABASE)

`python3 manage.py analyze_html_in_database --base-url "https://education.byu.edu" --css-directory "/Volumes/education22/Education/web/themes/custom/canvas/css" --js-directory "/Volumes/education22/Education/web/themes/custom/canvas"`

`--base-url` (required): What website you are searching the directories for  
`--css-directory` (required): What directory do you want to search for css files?  
`--js-directoy` (required): same as css-directory

### Search for usage of specific class and/or highest usage classes

`python3 manage.py css_usage --base-url "https://education.byu.edu" --html-attribute .whatever`  
  
`--html-attribute` is the attribute you want to search for (optional)

## Feel free to progam more commands in `csscleanup/apps/scraper/management/commands`
Here are some that could be useful:
1. A command that searches where a specific html attribute is used in the html (can use HtmlPage object)
2. A command that shows where a CSS style is in the css files in a diretory

## Project setup
Assuming you're using vscode you will want to:
1. Clone the repo.
    1. Open the terminal and navigate to the folder you want the repo folder to be in.
    2. Use the command `git clone https://github.com/MSE-Web-Team/css-cleanup-helper.git`
2. Get a database that the script can use to scrape the website using the command above.
    * When it has been created, place it in the "csscleanup" folder (not the "css-cleanup-helper" folder)
    * Ensure it is named `db.sqlite3`.
3. Create and activate a python virtual environment.
    1. in the root directory of the project, use `python3 -m venv venv`.
    2. Use `source venv/bin/activate`
        * NOTE: to exit the python virtual environment, use the `deactivate` command.
4. Install dependencies
    1. Use `pip install -r requirements.txt`
    * Ensure you are using the venv Python interpreter.
        1. Hit command + shift + p and search for "Python: Select Interpreter".
        2. look for the one named "venv" and select it.
