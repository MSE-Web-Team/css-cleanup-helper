import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.parse import urljoin
import ssl
import warnings
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

warnings.simplefilter("ignore")

# Regex pattern to match a URL
HTTP_URL_PATTERN = r'^http[s]*://.+'

# Create a class to parse the HTML and get the hyperlinks
class HyperlinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # Create a list to store the hyperlinks
        self.hyperlinks = []

    # Override the HTMLParser's handle_starttag method to get the hyperlinks
    def handle_starttag(self,tag, attrs):
        attrs = dict(attrs)

        # If the tag is an anchor tag and it has an href attribute, add the href attribute to the list of hyperlinks
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])
        elif tag == "link" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])
        elif tag == "script" and "src" in attrs:
            self.hyperlinks.append(attrs["src"])

class Scraper:
    def __init__(self,base_url,output_dir,driver,verbose,use_sitemap,custom_localdomain,force_https):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        if len(os.listdir(output_dir)) > 0:
            print(f"Output directory '{output_dir}' already has files!\nExiting...")
            exit(1)
    
        match driver:
            case "chrome":
                pass
            case "edge":
                pass
            case "firefox":
                pass
            case "safari":
                pass
            case _:
                print(f"Error: given webdriver '{driver}' is not valid. Please give one of the following options: chrome, edge, firefox, safari")
                exit(1)
        
        self.base_url = base_url
        self.output_dir = output_dir
        self.webdriver = driver
        self.verbose = verbose
        self.use_sitemap = use_sitemap
        self.custom_localdomain = custom_localdomain
        self.force_https = force_https
    
    def scrape(self):
        """
        Initiates the website scraping process.
        """
        if self.verbose:
            print("Starting to scrape")
            if self.use_sitemap:
                print("Using sitemap.xml")
        
        """
        Scrapes the website starting from the given URL.
        """
        url = self.base_url
        local_domain = urlparse(url).netloc
        start = url
        if self.use_sitemap:
            start = urljoin(start,"sitemap.xml")
        queue = deque([start])
        seen = set([start])
        # edge_options = Options()
        # edge_options.add_argument("--disable-extensions")

        driver = None
        match self.webdriver:
            case "chrome":
                driver = webdriver.Chrome()
            case "edge":
                driver = webdriver.Edge()
            case "firefox":
                driver = webdriver.Firefox()
            case "safari":
                driver = webdriver.Safari()

        while queue:
            url = queue.pop()
            if string_contains_extension(url):
                if self.verbose:
                    print(f" - Skipping because it is a file/invalid: {url}")
                continue
            response = requests.get(url, verify=False)
            if is_not_page(response):
                if self.verbose:
                    print(f" - Skipping because not a page: {url}")
                continue
            if response.status_code != 200:
                if self.verbose:
                    print(f" - Skipping because status code not 200: {url}")
                continue
            print(f" + {url}")
            content_type = response.headers.get('content-type')
            if 'text/css' in content_type or 'application/javascript' in content_type:
                self.create_page(url,response.content)
                continue
            driver.implicitly_wait(0.5) # seconds
            driver.get(url)
            html_text = driver.page_source
            soup = BeautifulSoup(driver.page_source, "html.parser")
            title = url
            if soup.find('title'):
                title = soup.find('title').text
            # Here we will now generate the necessary model for the url
            self.create_page(url,html_text)
            # If the crawler gets to a page that requires JavaScript, it will stop the crawl
            if ("You need to enable JavaScript to run this app." in html_text):
                print(f"Unable to parse page {url} due to JavaScript being required")
            # Get the hyperlinks from the URL and add them to the queue
            for link in self.get_domain_hyperlinks(local_domain, html_text):
                #create_html_link(html_page_object, link)
                if link not in seen:
                    queue.append(link)
                    seen.add(link)
        driver.close()

        if self.verbose:
            print("Finished scraping")
    
    def create_page(self,url,content):
        url_path = urlparse(url).path
        out_path = os.path.join(self.output_dir,url_path[1:])
        if os.path.splitext(out_path)[1] == '':
            out_path = os.path.join(out_path,"index.html")
        os.makedirs(os.path.dirname(out_path),exist_ok=True)
        if type(content) == str:
            with open(out_path,"w") as f:
                f.write(content)
        else:
            with open(out_path,"wb") as f:
                f.write(content)
        
    
    # Function to get the hyperlinks from a URL that are within the same domain
    def get_domain_hyperlinks(self,local_domain, html_text):
        clean_links = []
        for link in set(get_hyperlinks(html_text)):
            clean_link = None
            # If the link is a URL, check if it is within the same domain
            if re.search(HTTP_URL_PATTERN, link):
                # Parse the URL and check if the domain is the same
                url_obj = urlparse(link)
                if url_obj.netloc == local_domain:
                    clean_link = link
                elif url_obj.netloc == self.custom_localdomain:
                    protocol = url_obj.scheme
                    clean_link = f"{protocol}://{local_domain}{url_obj.path}"
                    pass
            # If the link is not a URL, check if it is a relative link
            else:
                if link.startswith("/"):
                    link = link[1:]
                if link.startswith("../../"):
                    link = link[6:]
                elif link.startswith("#") or link.startswith("mailto:"):
                    continue
                clean_link = "https://" + local_domain + "/" + link
            if clean_link is not None:
                url_obj = urlparse(clean_link)
                protocol = url_obj.scheme
                if self.force_https:
                        protocol = "https" #force https for sitemap
                clean_link = f"{protocol}://{url_obj.netloc}{url_obj.path}"
                if clean_link.endswith("/"):
                    clean_link = clean_link[:-1]
                clean_links.append(clean_link)
        # Return the list of hyperlinks that are within the same domain
        return list(set(clean_links))

# Function to get the hyperlinks from a URL
def get_hyperlinks(html_text):
    parser = HyperlinkParser()
    parser.feed(html_text)
    return parser.hyperlinks

def string_contains_extension(url):
    """
    Checks if a URL contains a file extension or other indicators that it is not a web page.
    """
    if not url:
        return False
    file_extensions = ['�', 'email:', '@gmail', '.com', '@yahoo', '.txt', '.pdf', '.edu?', 'edlf/newsletters',
                       'clientredirect?', 'shared/code', '.php', '.pdf', '.docx', '.xlsx', '.png', '.jpg', '.jpeg',
                       "#", "tel:", "/files/media"]
    for char in file_extensions:
        if char in url:
            return True
    return False

def is_not_page(response):
    """
    Checks if the response corresponds to a web page.
    """
    content_type = response.headers.get('content-type')
    #print(content_type)
    return 'text/html' not in content_type and 'text/css' not in content_type and 'text/xml' not in content_type and 'application/javascript' not in content_type

def sanitize(string):
    """
    Sanitizes a string by removing unnecessary characters and extra spaces.
    """
    string = string.replace('\n', ' ')
    string = string.replace('\\n', ' ')
    string = string.replace('  ', ' ')
    string = string.replace('yu.edu', '')
    string = string.replace('  ', ' ')
    string = string.replace('    ', '')
    string = re.sub(r'\s+', ' ', string)
    return string
