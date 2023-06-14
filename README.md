
# Css Cleanup Helper
This tool allows you to scrape the current contents of a site and detect where links are used, css classes, and html elements.

# How to use
1. Download the repository
2. Install requirements.txt (`python3 -m pip install -r ./requirements.txt`)
3. Migrate the database (`python3 manage.py makemigrations && python3 manage.py migrate`)
4. Make a .env file in the settings folder with the following text
```
    SECRET_KEY=anything_good_here
```
5. Install the Webdrive for Edge (https://selenium-python.readthedocs.io/installation.html)
6. Run the commands in the Commands section

# Commands
### Convert website into database entries

`python manage.py scrape --base-url https://education.byu.edu`

`--base-url` (required): The base where you would like the scrapper to start.

### Search for css stylesheets that are unused

`python3 manage.py analyze_html_in_database --base-url "https://education.byu.edu" --css-directory "/Volumes/education22/Education/web/themes/custom/canvas/css" --js-directory "/Volumes/education22/Education/web/themes/custom/canvas"`

`--base-url` (required): What website you are searching the directories for
`--css-directory` (required): What directory do you want to search for css files?
`--js-directoy` (required): same as css-directory

### Search for usage of specific class and/or highest usage classes

`python3 manage.py css_usage --base-url "https://education.byu.edu" --html-attribute .whatever`

`--html-attribute` is the attribute you want to search for (optional)