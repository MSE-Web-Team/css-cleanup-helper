
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
    2. Install a [Webdriver](https://selenium-python.readthedocs.io/installation.html) for the browser you wish to scrape the site with.
4. Scrape the site (`python3 css.py scrape --base-url https://education.byu.edu/ --output-dir clone/ --webdriver chrome --verbose --use-sitemap`  )
    * Replace the webdriver with whatever web browser you want to use to scrape (options are chrome,firefox,edge, and safari)
    * You can try scraping a local site, but ddev seems to have issues with https on some pages
5. Analyze the local clone of the site (`python3 css.py analyze --html-dir clone/ --markdown-dir output --verbose`)
    1. This will take some time (especially if the --inline-styles flag is used)
    2. The output will be in markdown files in the directory defined by --markdown-dir

## Commands -
### Scrape the website

`python3 css.py scrape --base-url https://education.byu.edu/ --output-dir clone/ --webdriver chrome --verbose --use-sitemap`  
  
`--base-url` (required): The base where you would like the scrapper to start.   
`--output-dir` (required): The directory where the cloned site content will go  
`--webdriver` (required): The webdriver that selinium will use to scrape the site with (Options are chrome, firefox, edge, and safari)  
`--verbose`: Print extra output to the console  
`--quiet`: Print less output to thte console    
`--use-sitemap`: Start the scrape at /sitemap.xml to hit more pages  
`--no-use-sitemap`: Don't start the scrape at /sitemap.xml  
`--custom-localdomain`: Allow resources from a given domain to the accessed as if they were on the same site    
`--force-https`: Force the scraper to use https   
`--no-force-https`: Opposite of --force-https   

### Analyze the website

`python3 css.py analyze --html-dir clone/ --markdown-dir output --verbose`

`--html-dir` (required): The root directory of the cloned website    
`--markdown-dir` (required): The directory the output markdown files will go into    
`--verbose`: Print extra output    
`--quiet`: Print less output    
`--inline-styles`: Treat html <style> tags like css stylesheets    
`--no-inline-styles`: Don't treat html <style> tags like css stylesheets    

## Generated Files

### all_class_use.md

all_class_use.md is a very large markdown file that includes every css class or index selector, which html files they are used in, and how many times they are used in that file.  
To find where a class is used, just search for 'class_name' in the all_class_use.md file.

### class_usage.md

This file includes a list of every class/id used in the project, the stylesheet it comes from, and how many times it was used overall.  
Note: this also includes classes that aren't used at all. To find unused classes in a stylesheet, do a search for the stylesheet name in class_usage.md, and search until you find the first occurence with 0 uses. They should all be sorted together from there.  

### not_defined_classes.md

This file has a list of every class or id that was in an html file, but not in a stylesheet.  

### stylesheets.md

This file includes a list of every stylesheet inside of the website that was referenced by an html file.  

It has several collumns that are useful for cleaning up css:  
`File`: The location/name of the stylesheet  
`Exists`: Whether or not the file exists in the cloned website directory  
`Is Inline`: True if the stylesheet was created from an html <style> tag (only applicable if --inline-styles was passed into the analyze command)  
`Number of Classes`: The total number of CSS classes in the stylesheet  
`Number of IDs`: The total number of CSS id selectors in the stylesheet  
`Class Uses`: How many times classes from this stylesheet were used on the entire site  
`Id Uses`: How many times ids from this stylesheet were used on the entire site  
`Unused Classes+IDs`: The number of classes and IDs from this stylesheet that went unused on the entire site. (See class_usage.md for a list of these)  
