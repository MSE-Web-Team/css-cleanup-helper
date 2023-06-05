import datetime
from django.core.management.base import BaseCommand, CommandError
from csscleanup.apps.scraper.models import HtmlBaseUrl, HtmlElement
from django.utils.translation import gettext as _
import requests
import re
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
import urllib
import os
import re
import ssl
from collections import defaultdict


class Command(BaseCommand):
    help = 'Finds where classes are used on page'

    def add_arguments(self, parser):
        parser.add_argument('--base-url', type=str)
        parser.add_argument('--css-path', type=str)
    
    def handle(self, *args, **options):
        # Check if base url is provided
        if options['base_url'] is None or options['css_path'] is None:
            raise CommandError('Please provide base url and css path')

        url = options['base_url']
        css_file = options['css_path']

        # Retrieve HtmlBaseUrlObject
        HtmlBaseUrlObject = HtmlBaseUrl.objects.get(url=url)

        # Read the CSS file
        with open(css_file, 'r') as f:
            css_content = f.read()

        # Extract class selectors and ID selectors using regular expressions
        class_selectors = re.findall(r'\.[a-zA-Z0-9_-]+', css_content)
        id_selectors = re.findall(r'#[a-zA-Z0-9_-]+', css_content)

        # Collect selectors to process
        selectors = class_selectors + id_selectors

        # Collect elements related to the selectors
        elements_by_selector = defaultdict(list)
        elements_not_used = set()
        elements_less_than_5 = set()

        elements_queryset = HtmlElement.objects.filter(related_base_url=HtmlBaseUrlObject, html_element__in=selectors)
        elements_queryset = elements_queryset.only('html_element', 'page_url')

        for element in elements_queryset:
            elements_by_selector[element.html_element].append(element)

        # Process selectors and collect results
        for selector in selectors:
            elements = elements_by_selector[selector]
            count = len(elements)

            if selector in elements_not_used or selector in elements_less_than_5:
                continue

            if count < 1:
                elements_not_used.add(selector)
            elif count < 6:
                elements_less_than_5.add(f"{selector} - {count}")

            if selector in elements_not_used or selector in elements_less_than_5:
                continue

            url_set = set(element.page_url for element in elements)

            # Track the page count directly instead of maintaining a separate counter
            page_count = len(url_set)

        # Convert sets to lists for printing
        not_used = list(elements_not_used)
        less_than_5 = list(elements_less_than_5)

        # Print the results
        print(f"Not used: {not_used}")
        print(f"Used 5 or less times: {less_than_5}")
