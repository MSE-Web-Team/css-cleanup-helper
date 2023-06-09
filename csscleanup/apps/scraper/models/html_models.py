from django.db import models

class HtmlBaseUrl(models.Model):
    url = models.CharField(max_length=200, default="")
    is_scraped = models.BooleanField(default=False)

class HtmlPage(models.Model):
    related_base_url = models.ForeignKey(HtmlBaseUrl, on_delete=models.CASCADE)
    page_url = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=300, default="")
    html = models.TextField(default = "")

# Stores the base url
class HtmlElement(models.Model):
    related_base_url = models.ForeignKey(HtmlBaseUrl, on_delete=models.CASCADE)
    related_html_page = models.ForeignKey(HtmlPage, on_delete=models.CASCADE)
    html_element = models.CharField(max_length=200, default="")

class HtmlLink(models.Model):
    related_html_page = models.ForeignKey(HtmlPage, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, default="")

