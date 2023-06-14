import datetime
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement, HtmlPage, HtmlLink, HtmlSource,HtmlSourceAttribute
import os, re
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
        HtmlElement.objects.filter(related_base_url=base_url).delete()
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
                if not obj.found_in_site_html:
                    obj.found_in_site_html = True
                    obj.save()
        for link_tag in soup.find_all('link'):
            href = link_tag.get('href')
            if href:
                obj, created = HtmlSource.objects.get_or_create(source=href, defaults={'source': href, 'related_base_url': related_base_url, 'source_type': "css"})
                if not created:
                    obj.found_in_site_html = True
                    obj.save()
        
        # Loop through page and store all classes on the site.
        for html_element in soup.find_all(class_=True):
            classes = html_element.get('class')
            for html_class in classes:
                obj, created = HtmlElement.objects.get_or_create(related_base_url = related_base_url, html_attribute=f".{html_class}", 
                defaults={'html_attribute':f".{html_class}", 'related_base_url': related_base_url, 'related_html_page': page})
                if not created:
                    obj.usage_count = obj.usage_count + 1
                    obj.save()

    def analyzeDirectory(self, related_base_url, css_file_paths, js_file_paths):
        # Pull on sources found on the website
        class_pattern = r"\.([^\s{]+)"
        bracket_pattern = r"\[[^\]]*\]"
        css_sources = HtmlSource.objects.filter(related_base_url=related_base_url, source_type="css", found_in_site_html = True)
        js_sources = HtmlSource.objects.filter(related_base_url=related_base_url, source_type="javascript", found_in_site_html = True)
        unused_css_files = []
        unused_js_files = []


        # Here we loop through all the css/js files in the specified directory and check if they are used on the site
        for css_file in css_file_paths:
            used_source = None
            unused = True
            for source in css_sources:
                # If the css file name is found in the source, mark the source as used.
                if css_file["file_name"] in source.source:
                    used_source = source
                    print(css_file["file_path"])
                    unused = False
                    source.server_relative_url = css_file["file_path"]
                    source.save()
                    break
            if unused:
                # Create unused source out of the css_file
                obj, created = HtmlSource.objects.get_or_create(source=css_file["file_path"], defaults={'source': css_file["file_path"], 'related_base_url': related_base_url, 'source_type': "css", 'found_in_site_html': False})
                used_source = obj
            
            # Now we w
            with open(css_file["file_path"], "r") as css_file:
                file_contents = css_file.read()
            css_classes = re.findall(class_pattern, file_contents)
            css_classes = [re.sub(r":[^:]+", "", cls) for cls in css_classes]
            if len(css_classes) > 0:
                # Remove content enclosed in square brackets
                css_classes = [re.sub(bracket_pattern, "", cls) for cls in css_classes]

                # Split CSS classes separated by commas and remove leading/trailing whitespace
                css_classes = [cls.strip() for cls in ",".join(css_classes).split(",")]
                css_classes = [cls.strip() for cls in ".".join(css_classes).split(".")]
                css_classes = [cls.strip() for cls in ">".join(css_classes).split(">")]
                css_classes = [cls for cls in css_classes if ')' not in cls and ';' not in cls]

                for css_class in css_classes:
                    database_element = HtmlElement.objects.filter(related_base_url=related_base_url, html_attribute = f".{css_class}")
                    found_in_site_html = False
                    if database_element:
                        found_in_site_html = True
                    obj,created = HtmlSourceAttribute.objects.get_or_create(related_html_source = used_source, html_attribute = f".{css_class}", defaults={'related_html_source': used_source, 'html_attribute': f".{css_class}", 'found_in_site_html': found_in_site_html})
                    if not created:
                        obj.found_in_site_html = found_in_site_html


        for js_file in js_file_paths:
            unused = True
            for source in js_sources:
                # If true this means that this file is used
                if js_file["file_name"] in source.source:
                    unused = False
                    source.server_relative_url = js_file["file_path"]
                    source.save()
                    break
            if unused:
                # Create unused source out of the js_file
                obj, created = HtmlSource.objects.get_or_create(source=js_file["file_path"], defaults={'source': js_file["file_path"], 'related_base_url': related_base_url, 'source_type': "javascript", "found_in_site_html": False})
            
        
        


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
