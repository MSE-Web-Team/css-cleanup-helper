import datetime
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement, HtmlPage, HtmlLink, HtmlSource
import os
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Analyzes all pages of parent base-url and inserts necessary information into the database for analysis'

    def add_arguments(self, parser):
        parser.add_argument('--base-url', type=str)
        parser.add_argument('--css-directory', type=str)
        parser.add_argument('--js-directory', type=str)

    def handle(self, *args, **options):
        # code for html analysis
        if options['base_url'] is None or options['css_directory'] is None or options['js_directory'] is None:
            raise CommandError('Please provide base-url, css-directory, and js-directory flag')

        css_directory = options['css_directory']
        js_directory = options['js_directory']
        # /Volumes/education22/Education/web/themes
        # Gets the css and js file paths to analyze
        css_file_paths = find_files(css_directory, ".css")
        js_file_paths = find_files(js_directory, ".js")

        # Get all pages stored in the database by base url
        base_url = HtmlBaseUrl.objects.get(url = options['base_url'])
        html_pages = HtmlPage.objects.filter(related_base_url = base_url)
        for page in html_pages:
            self.analyzeSources(base_url, page)
        
        self.analyzeDirectory(base_url, css_file_paths, js_file_paths)

    def analyzeSources(self, related_base_url, page):
        # Analyze all <link> and <script> tags for sources and inserts used ones into database
        soup = BeautifulSoup(page.html, 'html.parser')

        # Get all script and link tags with their sources inside the page html
        for script_tag in soup.find_all('script'):
            src = script_tag.get('src')
            if src:
                obj, created = HtmlSource.objects.get_or_create(source=src, defaults={'source': src, 'related_base_url': related_base_url, 'source_type': "javascript"})

        for link_tag in soup.find_all('link'):
            href = link_tag.get('href')
            if href:
                obj, created = HtmlSource.objects.get_or_create(source=href, defaults={'source': href, 'related_base_url': related_base_url, 'source_type': "css"})

    def analyzeDirectory(self, related_base_url, css_file_paths, js_file_paths):
        css_sources = HtmlSource.objects.filter(related_base_url=related_base_url, source_type="css")
        js_sources = HtmlSource.objects.filter(related_base_url=related_base_url, source_type="javascript")
        unused_css_files = []
        unused_js_files = []

        css_file_names = {css_file["file_name"] for css_file in css_file_paths}
        js_file_names = {js_file["file_name"] for js_file in js_file_paths}

        for css_file_name in css_file_names:
            unused = True
            for source in css_sources:
                if css_file_name in source.source:
                    unused = False
                    break
            if unused:
                unused_css_files.append(css_file_name)


        for js_file_name in js_file_names:
            unused = True
            for source in js_sources:
                if js_file_name in source.source:
                    unused = False
                    break
            if unused:
                unused_js_files.append(js_file_name)



        print(unused_css_files)
        print(unused_js_files)
            
        
        


def find_files(directory, file_extension):
    files_found = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_map = {"file_path":"","file_name":""}
            if file.endswith(file_extension):
                file_map["file_name"] = os.path.basename(os.path.join(root, file))
                file_map["file_path"] = os.path.join(root, file)
                files_found.append(file_map)
    return files_found
