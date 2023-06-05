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
import ssl

class Command(BaseCommand):
    help = 'Finds where classes are used on page'

    def add_arguments(self, parser):
        parser.add_argument('--base-url', type=str)
        parser.add_argument('--attribute-value', type=str)
    
    def handle(self, *args, **options):
        # Check if base url is provided
        if options['base_url'] is None or options['attribute_value'] is None:
            raise CommandError('Please provide base url and attribute value')
        url = options['base_url']
        attribute_value = options['attribute_value']
        HtmlBaseUrlObject = HtmlBaseUrl.objects.get(url=url)
        AllHtmlElements = HtmlElement.objects.filter(related_base_url=HtmlBaseUrlObject, html_element=attribute_value)
        print(f"Total amount of elements: { AllHtmlElements.count() }")

        url_list = []
        page_count = 0

        for element in AllHtmlElements:
            page_url = element.page_url
            if page_url not in url_list:
                page_count += 1
                url_list.append(page_url)
                print(page_url)
        
        print(f"Used on {page_count} pages")


