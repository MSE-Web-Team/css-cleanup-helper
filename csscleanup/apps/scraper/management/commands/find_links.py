import datetime
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement, HtmlPage, HtmlLink

class Command(BaseCommand):
    help = 'Finds where a link is used on the scraped page'

    def add_arguments(self, parser):
        parser.add_argument('--find-url', type=str)

    def handle(self, *args, **options):
        if options['find_url'] is None:
            raise CommandError('Please provide a URL to search for')

        url = options['find_url']
        links = HtmlLink.objects.filter(link=url)
        print(f"Found {len(links)} links")
        for link in links:
            print(link.related_html_page.page_url)