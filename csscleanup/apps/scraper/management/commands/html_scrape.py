import datetime
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement, HtmlPage, HtmlLink
from django.utils.translation import gettext as _
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
import urllib
import os
import ssl
import warnings

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
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        # If the tag is an anchor tag and it has an href attribute, add the href attribute to the list of hyperlinks
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])

class Command(BaseCommand):
    help = 'Scrapes a website and stores the results in the database'

    def add_arguments(self, parser):
        parser.add_argument('--base-url', type=str)

    def handle(self, *args, **options):
        if options['base_url'] is None:
            raise CommandError('Please provide a base URL')

        if self.delete_all_html_base_urls(options['base_url']):
            self.start_scrape(options['base_url'])

    def delete_all_html_base_urls(self, base_url):
        """
        Deletes all references to the base URL and creates a new HtmlBaseUrl object.
        """
        html_base_url_objects = HtmlBaseUrl.objects.filter(url=base_url)
        if len(html_base_url_objects) > 0:
            print("We will delete all references to this base URL before proceeding.")
            confirm = input(_('Please confirm the deletion process by typing (yes/no)'))
            if confirm != 'yes':
                print("Aborting...")
                return False
        print("Deleting all references to this base URL")
        HtmlBaseUrl.objects.filter(url=base_url).delete()
        print("Creating HtmlBaseUrl object")
        HtmlBaseUrl.objects.create(url=base_url)
        return True

    def start_scrape(self, base_url):
        """
        Initiates the website scraping process.
        """
        print("Starting to scrape")
        self.scrape(base_url)
        self.finish_scrape(base_url)
        print("Finished scraping")

    def scrape(self, url):
        """
        Scrapes the website starting from the given URL.
        """
        local_domain = urlparse(url).netloc
        queue = deque([url])
        seen = set([url])
        html_base_url_object = HtmlBaseUrl.objects.get(url=url)

        # edge_options = Options()
        # edge_options.add_argument("--disable-extensions")

        driver = webdriver.Edge()
        
        while queue:
            url = queue.pop()
            if self.string_contains_extension(url):
                print(" - Skipping because it is a file/invalid: " + url)
                continue
            response = requests.get(url, verify=False)
            if self.is_not_page(response):
                print(" - Skipping because not a page: " + url)
                continue
            if response.status_code != 200:
                print(" - Skipping because status code not 200: " + url)
                continue
            print(" + " + url)

            
            driver.implicitly_wait(0.5) # seconds
            driver.get(url)

            html_text = driver.page_source
            soup = BeautifulSoup(driver.page_source, "html.parser")
            title = url
            if soup.find('title'):
                title = soup.find('title').text

            # Here we will now generate the necessary model for the url
            html_page_object = self.create_html_page(html_base_url_object, url, title, html_text)

            # If the crawler gets to a page that requires JavaScript, it will stop the crawl
            if ("You need to enable JavaScript to run this app." in html_text):
                print("Unable to parse page " + url + " due to JavaScript being required")
            

            # Get the hyperlinks from the URL and add them to the queue
            for link in self.get_domain_hyperlinks(local_domain, url, html_text):
                self.create_html_link(html_page_object, link)
                if link not in seen:
                    queue.append(link)
                    seen.add(link)
        driver.close()

    # Function to get the hyperlinks from a URL
    def get_hyperlinks(self, html_text):
        parser = HyperlinkParser()
        parser.feed(html_text)

        return parser.hyperlinks

    # Function to get the hyperlinks from a URL that are within the same domain
    def get_domain_hyperlinks(self, local_domain, html_text):
        clean_links = []
        for link in set(self.get_hyperlinks(html_text)):
            clean_link = None

            # If the link is a URL, check if it is within the same domain
            if re.search(HTTP_URL_PATTERN, link):
                # Parse the URL and check if the domain is the same
                url_obj = urlparse(link)
                if url_obj.netloc == local_domain:
                    clean_link = link

            # If the link is not a URL, check if it is a relative link
            else:
                if link.startswith("/"):
                    link = link[1:]
                elif link.startswith("#") or link.startswith("mailto:"):
                    continue
                clean_link = "https://" + local_domain + "/" + link

            if clean_link is not None:
                if clean_link.endswith("/"):
                    clean_link = clean_link[:-1]
                clean_links.append(clean_link)

        # Return the list of hyperlinks that are within the same domain
        return list(set(clean_links))

    def string_contains_extension(self, url):
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

    def is_not_page(self, response):
        """
        Checks if the response corresponds to a web page.
        """
        content_type = response.headers.get('content-type')
        return 'text/html' not in content_type

    def finish_scrape(self, base_url):
        """
        Marks the scraping process as finished for the given base URL.
        """
        HtmlBaseUrl.objects.filter(url=base_url).update(is_scraped=True)

    def create_html_element(self, html_base_url, html_page, html_element):
        """
        Creates a new HtmlElement object and stores it in the database.
        """
        return HtmlElement.objects.create(
            related_base_url=html_base_url,
            related_html_page=html_page,
            html_element=html_element
        )
    
    def create_html_page(self, html_base_url, page_url, title, html):
        """
        Creates a new HtmlPage object and stores it in the database
        """
        return HtmlPage.objects.create(
            related_base_url = html_base_url,
            page_url = page_url,
            title = title,
            html = html,
        )

    def create_html_link(self, html_page, link):
        """
        Creates a new html link objects and stores it in the database
        """
        return HtmlLink.objects.create(
            related_html_page = html_page,
            link = link
        )


    def sanitize(self, string):
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
