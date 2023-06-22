import datetime, re
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement, HtmlPage, HtmlLink

class_pattern = r"\.([^\s{]+)"
bracket_pattern = r"\[[^\]]*\]"

class Command(BaseCommand):
    help = 'Shows the usage of html elements in a css stylesheet'

    def add_arguments(self, parser):
        parser.add_argument('--base-url', type=str)
        parser.add_argument('--css-file-path', type=str)

    def handle(self, *args, **options):
        if options['base_url'] is None:
            raise CommandError('Please provide a URL to search for (--base-url)')
        print("--html-attribute is optional and can be used to select the usage of a single html_attribute")

        url = options['base_url']
        base_url = HtmlBaseUrl.objects.get(url=url)
        html_attribute = ""

        with open(options["css_file_path"], "r") as css_file:
            file_contents = css_file.read()
        css_classes = re.findall(class_pattern, file_contents)
        css_classes = [re.sub(r":[^:]+", "", cls) for cls in css_classes]
        for css_class in css_classes:
            element = HtmlElement.objects.filter(related_base_url=base_url).filter(html_attribute=f".{css_class}")
            if(element):
                print(element.html_attribute + ": Used " + str(element.usage_count))
            else:
                print(f".{css_class}: Used 0 times")