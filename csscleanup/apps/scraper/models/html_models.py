from django.db import models

class HtmlBaseUrl(models.Model):
    url = models.CharField(max_length=200, default="")
    is_scraped = models.BooleanField(default=False)

    def __str__(self):
        return self.url

class HtmlPage(models.Model):
    related_base_url = models.ForeignKey(HtmlBaseUrl, on_delete=models.CASCADE)
    page_url = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=300, default="")
    html = models.TextField(default = "")

    def __str__(self):
        return self.title

# Stores the base url
class HtmlElement(models.Model):
    related_base_url = models.ForeignKey(HtmlBaseUrl, on_delete=models.CASCADE)
    related_html_page = models.ForeignKey(HtmlPage, on_delete=models.CASCADE)
    html_attribute = models.CharField(max_length=200, default="")
    usage_count = models.IntegerField(default=1)

class HtmlLink(models.Model):
    related_html_page = models.ForeignKey(HtmlPage, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, default="")

class HtmlSource(models.Model):
    related_base_url = models.ForeignKey(HtmlBaseUrl, on_delete=models.CASCADE)
    source = models.CharField(max_length=500, default="")
    server_relative_url = models.CharField(max_length=500, default="")
    source_type = models.CharField(max_length=500, default="css")
    found_in_site_html = models.BooleanField(default=True)

class HtmlSourceAttribute(models.Model):
    related_html_source = models.ForeignKey(HtmlSource, on_delete=models.CASCADE)
    html_attribute = models.CharField(max_length=200, default="")
    found_in_site_html = models.BooleanField(default=False)

