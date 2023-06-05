
# Website to chatbot
This tool allows you to scrape the current contents of a site and detect where links are used, css classes, and html elements.

# How to use
1. Download the repository
2. Install requirements.txt (python3 -m pip install -r ./requirements.txt)
3. Migrate the database (python3 manage.py makemigrations && python3 manage.py migrate)
4. Make a .env file in the settings folder with the following text
```
    SECRET_KEY=anything_good_here
```
5. Run the commands in the Commands section

# Commands
### Convert website into database entries

python manage.py scrape --base-url https://education.byu.edu

--base-url (required): The base where you would like the scrapper to start.

### Search for pages where links are used
python manage.py find_links --find-url inserturlhere
