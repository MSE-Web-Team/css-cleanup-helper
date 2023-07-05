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
        unique = []
        classes = {}
        for css_class in css_classes:
            # Please don't kill me, feel free to turn this into an array :)
            if(css_class not in unique and ")" not in css_class and ";" not in css_class and "}" not in css_class and "{" not in css_class and "'" not in css_class and "`" not in css_class and "," not in css_class and "rem" not in css_class and "7s" not in css_class):
                unique.append(css_class)
                element = HtmlElement.objects.filter(related_base_url=base_url).filter(html_attribute=f".{css_class}").first()
                if(element):
                    classes[f".{css_class}"] = int(element.usage_count)
                else:
                    classes[f".{css_class}"] = 0
                    
        dict(sorted(classes.items(), key=lambda item: item[1]))
        print(classes)