import datetime
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement, HtmlPage, HtmlLink

class Command(BaseCommand):
    help = 'Shows the usage of html elements'

    def add_arguments(self, parser):
        parser.add_argument('--base-url', type=str)
        parser.add_argument('--html-attribute', type=str)
        parser.add_argument('--verbose', action='store_true', help='print the paths to the locations found')

    def handle(self, *args, **options):
        if options['base_url'] is None:
            raise CommandError('Please provide a URL to search for (--base-url)')
        print("--html-attribute is optional and can be used to select the usage of a single html_attribute")

        url = options['base_url']
        base_url = HtmlBaseUrl.objects.get(url=url)
        html_attribute = ""
        if(options['html_attribute']):
            html_attribute = options['html_attribute']
        if(html_attribute != ""):
            elements = HtmlElement.objects.filter(related_base_url=base_url).filter(html_attribute=html_attribute)
        else:
            elements = HtmlElement.objects.all().filter(related_base_url=base_url).order_by('-usage_count')
        
        for element in elements:
            print(element.html_attribute + ": Used " + str(element.usage_count))