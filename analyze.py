from bs4 import BeautifulSoup
from glob import glob
import os
import cssutils

class HtmlClass:
    def __init__(self,name):
        self.name = name
        self.uses = 1

class HtmlClasses:
    def __init__(self):
        self.class_list = []
    
    def add_class(self,classname):
        found = False
        for html_class in self.class_list:
            if html_class.name == classname:
                found = True
                html_class.uses += 1
                break
        if not found:
            self.class_list.append(HtmlClass(classname))

    def sort(self):
        self.class_list.sort(key=lambda x: x.uses,reverse=True)
    
    def generate_table(self):
        self.sort()
        name_padding = len("Class Name")
        uses_padding = len("Uses")
        for html_class in self.class_list:
            if len(html_class.name) > name_padding:
                name_padding = len(html_class.name)
            if len(str(html_class.uses))>uses_padding:
                uses_padding = len(str(html_class.uses))
        table = "| "+"Class Name".ljust(name_padding," ")+" | "+"Uses".ljust(uses_padding," ")+" |\n"
        table += "| "+("-"*name_padding)+" | "+("-"*(uses_padding-1))+": |\n"
        for html_class in self.class_list:
            table += "| "+html_class.name.ljust(name_padding," ")+" | "+str(html_class.uses).rjust(uses_padding," ")+" |\n"
        return table

stylesheets = [
"core/modules/system/css/components/ajax-progress.module.css",
"core/modules/system/css/components/align.module.css",
"core/modules/system/css/components/autocomplete-loading.module.css",
"core/modules/system/css/components/fieldgroup.module.css",
"core/modules/system/css/components/container-inline.module.css",
"core/modules/system/css/components/clearfix.module.css",
"core/modules/system/css/components/details.module.css",
"core/modules/system/css/components/hidden.module.css",
"core/modules/system/css/components/item-list.module.css",
"core/modules/system/css/components/js.module.css",
"core/modules/system/css/components/nowrap.module.css",
"core/modules/system/css/components/position-container.module.css",
"core/modules/system/css/components/progress.module.css",
"core/modules/system/css/components/reset-appearance.module.css",
"core/modules/system/css/components/resize.module.css",
"core/modules/system/css/components/sticky-header.module.css",
"core/modules/system/css/components/system-status-counter.css",
"core/modules/system/css/components/system-status-report-counters.css",
"core/modules/system/css/components/system-status-report-general-info.css",
"core/modules/system/css/components/tabledrag.module.css",
"core/modules/system/css/components/tablesort.module.css",
"core/modules/system/css/components/tree-child.module.css",
"core/modules/filter/css/filter.caption.css",
"core/modules/media/css/filter.caption.css",
"core/modules/views/css/views.module.css",
"modules/contrib/flickity/vendor/flickity/flickity.min.css",
"themes/custom/canvas/less/styles.css",
"themes/custom/canvas/css/style.css",
"themes/custom/canvas/css/bootstrap.css",
"themes/custom/canvas/css/font-icons.css",
"themes/custom/canvas/css/imports/shortcodes/tabs.css",
"themes/custom/canvas/css/mckay-footer.css",
"themes/custom/canvas/css/mckay-menu.css",
"themes/custom/canvas/css/mckay-style.css"]

additional_stylesheets = [
"cas/css/cas.cs",
"modules/contrib/webform/css/webform.element.message.css",
"modules/contrib/webform/css/webform.form.css",
"modules/contrib/webform/css/webform.element.details.toggle.css",
"modules/contrib/webform/css/webform.ajax.css",
"core/modules/layout_discovery/layouts/onecol/onecol.css",
"modules/contrib/webform/css/webform.composite.css",
"modules/contrib/webform/css/webform.element.options.css",
"core/assets/vendor/jquery.ui/themes/base/core.css",
"core/assets/vendor/jquery.ui/themes/base/theme.css",
"themes/custom/canvas/third-party/3dflipbook/jquery-plugin/deploy/css/flipbook.style.css"]

#todo parse each stylesheet as it's added into the stylesheets array in analysisclass for BOTH classes and id selectors
#add a varible in the htmlclass class for source stylesheet (should be the html file if class comes from a style tag)
#parse all style tags if they exist in an html file

class AnalysisClass:
    def __init__(self,html_dir,markdown_dir,verbose):
        if not os.path.exists(html_dir):
            print(f"Error: directory '{html_dir}' doesn't exist!")
            exit(1)
        if len(os.listdir(html_dir)) == 0:
            print(f"Error: directory '{html_dir}' is empty!")
            exit(1)
        if not os.path.exists(markdown_dir):
            os.mkdir(markdown_dir)
        self.html_dir = html_dir
        self.markdown_dir = markdown_dir
        self.verbose = verbose
        self.classes = HtmlClasses()
        
    def start(self):
        cwd = os.getcwd()
        os.chdir(self.html_dir)
        html_files = glob("**/*.html",recursive=True)
        if self.verbose:
            print("Analyzing html files for class usage")
        for file in html_files:
            if self.verbose:
                print(f" Analyzing '{file}'")
            self.analyze_file(file)
            #break
        os.chdir(cwd)
        self.write_output()
    
    def analyze_file(self,file):
        with open(file,"r") as f:
            content = f.read()
            soup = BeautifulSoup(content,"html.parser")
            tags = {tag.name for tag in soup.find_all()}
            if "link" in tags:
                for link in soup.find_all("link"):
                    if link.has_attr("rel") and link["rel"][0]=="stylesheet" and link.has_attr("href") and link["href"][0]=='/':
                        stylesheet = link["href"]
                        if stylesheet.find("?"):
                            stylesheet = stylesheet[0:stylesheet.find("?")]
                        stylesheet = stylesheet[1:]
                        if stylesheet not in stylesheets:
                            print(stylesheet)
                            stylesheets.append(stylesheet)
            if "style" in tags:
                pass
            for tag in tags:
                for i in soup.find_all(tag):
                    if i.has_attr("class") and len(i["class"]) != 0:
                        for j in i["class"]:
                            self.classes.add_class(j)
    
    def write_output(self):
        os.chdir(self.markdown_dir)
        if self.verbose:
            print("Writing Class Usage Table")
        with open("class_usage.md","w") as f:
            f.write(self.classes.generate_table())
    
