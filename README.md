
# Css Cleanup Helper
This tool allows you to scrape the current contents of a site and detect where links are used, css classes, and html elements.

To Run: python3 css.py scrape --base-url https://education.byu.edu/ --output-dir clone/ --webdriver chrome --verbose True --use-sitemap True

## How to use
1. Clone the repo.
    1. Open the terminal and navigate to the directory you want the repo directory to be in.
    2. Use the command `git clone https://github.com/MSE-Web-Team/css-cleanup-helper.git`
2. Create and activate a python virtual environment.
    1. In the root directory of the project, use `python3 -m venv venv`.
    2. Run `source venv/bin/activate`
        * NOTE: to exit the python virtual environment, use the `deactivate` command.
3. Install dependencies
    1. Use `pip install -r requirements.txt`
    * If you are using vscode: Make sure you are using the venv Python interpreter.
        1. Hit control (or command) + shift + p and search for "Python: Select Interpreter".
        2. look for the one named "venv" and select it.
4. Get a database that the script can use to scrape the website using (`python3 manage.py makemigrations && python3 manage.py migrate`).
    * When it has been created, place it in the "csscleanup" directory (not the "css-cleanup-helper" directory)
    * Ensure it is in `csscleanup/db.sqlite3`
5. Scrape your local site (`python3 manage.py html_scrape --base-url https://127.0.0.1:32768/`  )

## Commands -
### Convert website into database entries (IF YOU DONT HAVE DATABASE)

`python manage.py scrape --base-url https://education.byu.edu`  
  
`--base-url` (required): The base where you would like the scrapper to start.

### Search for css stylesheets that are unused (IF YOU DONT HAVE DATABASE)

`python3 manage.py analyze_html_in_database --base-url "https://education.byu.edu" --css-directory "/Volumes/education22/Education/web/themes/custom/canvas/css" --js-directory "/Volumes/education22/Education/web/themes/custom/canvas"`

`--base-url` (required): What website you are searching the directories for  
`--css-directory` (required): What directory do you want to search for css files?  
`--js-directoy` (required): same as css-directory

### Search for usage of classes in a specific css stylesheet:

This isn't completely accurate as it will pull things like urls, and multiline classes like .card-title>h4 but it does an alright job at pulling the css classes. Obviously could be improved, but this was just put together in a couple minutes.

`python3 manage.py analyze_css_stylesheet --base-url "https://education.byu.edu" --css-file-path "PATH_TO_CSS_PATH"`

### Search for usage of specific class and/or highest usage classes

`python3 manage.py css_usage --base-url "https://education.byu.edu" --html-attribute .whatever`  
  
`--html-attribute` is the attribute you want to search for (optional)

## Feel free to progam more commands in `csscleanup/apps/scraper/management/commands`
Here are some that could be useful:
1. A command that searches where a specific html attribute is used in the html (can use HtmlPage object)
2. A command that shows where a CSS style is in the css files in a diretory
