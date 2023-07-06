import click
import scrape
import analyze

@click.group()
def css():
    pass

@css.command(name="scrape",help="Begin scraping the website from the given base-url into the output-dir using the given webdriver")
@click.option("--base-url",type=str,required=True,help="The URL to start scraping from.")
@click.option("--output-dir",type=str,required=True,help="The directory to start outputing the given files to")
@click.option("--webdriver",type=str,required=True,help="The webdriver to use. Options: chrome, edge, firefox, safari")
@click.option("--verbose/--quiet",required=False,default=False,help="Print extra info while scraping")
@click.option("--use-sitemap/--no-use-sitemap",required=False,default=True,help="Use the site's sitemap.xml as a starting place when scraping")
@click.option("--custom-localdomain",type=str,required=False,help="Allow a custom domain's resources to be accessed")
@click.option("--force-https/--no-force-https",required=False,default=False,help="Force any read hyperlink to use https")
def scrape_html(base_url,output_dir,webdriver,verbose,use_sitemap,custom_localdomain,force_https):
    scraper = scrape.Scraper(base_url,output_dir,webdriver,verbose,use_sitemap,custom_localdomain,force_https)
    scraper.scrape()

@css.command(name="analyze",help="Analyze the html from a given directory and produce a directory of markdown files with the results")
@click.option("--html-dir",type=str,required=True,help="The root directory for html to analyze")
@click.option("--markdown-dir",type=str,required=True,help="The directory the results will go into")
@click.option("--verbose/--quiet",required=False,help="Extra output",default=False)
def analyze_html(html_dir,markdown_dir,verbose):
    analysis = analyze.AnalysisClass(html_dir,markdown_dir,verbose)
    analysis.start()


if __name__ == "__main__":
    css()