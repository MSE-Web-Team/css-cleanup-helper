from bs4 import BeautifulSoup
from glob import glob
import os
import re

def generate_table(collumns,content):
    padding_list = list()
    table_string = "| "
    for i,collumn in enumerate(collumns):
        padding = len(collumn)
        for c in content[i]:
            if len(str(c))>padding:
                padding = len(str(c))
        padding_list.append(padding)
        if i != 0:
            table_string += " | "
        table_string += collumn.ljust(padding," ")
    table_string += " |\n| "
    for i,collumn in enumerate(collumns):
        if i != 0:
            table_string += " | "
        if type(content[i][0])==int:
            table_string += ('-'*(padding_list[i]-1))+':'
        else:
            table_string += ('-'*padding_list[i])
    table_string += " |\n"
    for j in range(len(content[0])):
        for i in range(len(collumns)):
            if i==0:
                table_string += "| "
            else:
                table_string += " | "
            if type(content[i][j]) == int:
                table_string += str(content[i][j]).rjust(padding_list[i]," ")
            else:
                table_string += str(content[i][j]).ljust(padding_list[i]," ")
            if i==len(collumns)-1:
                table_string += " |\n"
    return table_string

class HtmlClass:
    def __init__(self,name,origin):
        self.name = name
        self.origin = origin
        self.uses = 0
    
    def __eq__(self,other):
        return self.name == other

class HtmlClasses:
    def __init__(self):
        self.class_list = []
    
    def add_class(self,classname,origin):
        for html_class in self.class_list:
            if html_class.name == classname and html_class.origin == origin:
                return
        self.class_list.append(HtmlClass(classname,origin))

    def sort_by_uses(self):
        self.class_list.sort(key=lambda x: x.uses,reverse=True)

    def update_uses(self,classname):
        for html_class in self.class_list:
            if html_class.name == classname:
                html_class.uses += 1
                if classname[0] != "#":
                    html_class.origin.class_uses += 1
                else:
                    html_class.origin.id_uses += 1
                return True
        return False

    def generate_table_of_uses(self):
        self.sort_by_uses()
        name_table = []
        origin_table = []
        uses_table = []
        for _class in self.class_list:
            name_table.append(_class.name)
            origin_table.append(_class.origin.url)
            uses_table.append(_class.uses)
        table = generate_table(["Class Name","Origin","Uses"],[name_table,origin_table,uses_table])
        return table

class Stylesheet:
    def __init__(self,url,content,class_list):
        self.url = url
        self.exists = False
        self.classes = []
        self.inline = False
        self.id_selectors = []
        self.class_uses = 0
        self.id_uses = 0
        if content:
            self.inline = True
            self.exists = True
            self.parse(content)
        else:
            if os.path.exists(url):
                self.exists = True
                with open(self.url,"r") as f:
                    css = f.read()
                    self.parse(css)
        if self.exists:
            self.populate(class_list)

    def populate(self,class_list):
        for _class in self.classes:
            class_list.add_class(_class,self)
        for id in self.id_selectors:
            class_list.add_class(id,self)

    def parse(self,css):
        css = re.sub("\/\*[\s\S]*?\*\/","",css) #Remove comments
        #This method should get most of the class names, but it's not guranteed to get all of them
        classes = re.findall("\.[a-zA-Z_][\w:-]*(?![^\{]*\})",css)
        classes = self.remove_colon_from_names(classes)
        classes = list(set(classes))
        for i in range(len(classes)):
            classes[i] = classes[i].replace(".","")
        #print(f"Classes {self.url}: {classes}")
        ids = re.findall("\#[a-zA-Z_][\w:-]*(?![^\{]*\})",css)
        ids = self.remove_colon_from_names(ids)
        ids = list(set(ids))
        #print(f"IDs {self.url}: {ids}")
        self.classes = classes
        self.id_selectors = ids
    
    def remove_colon_from_names(self,names):
        updated_names = []
        for name in names:
            if name.find(":") == -1:
                updated_names.append(name)
        return updated_names
            
    def __repr__(self):
        return f"Stylesheet: '{self.url}' : Exists {self.exists} : Inline {self.inline}"

class Stylesheets:
    def __init__(self,classes,verbose):
        self.sheets = []
        self.class_list = classes
        self.verbose = verbose
    
    def add(self,url,content=None):
        found = False
        for sheet in self.sheets:
            if sheet.url == url:
                found = True
                break
        if not found:
            if self.verbose:
                print(f" Reading Stylesheet '{url}'")
            self.sheets.append(Stylesheet(url,content,self.class_list))
    
    def sort_by_number_of_classes(self):
        self.sheets.sort(key=lambda x: len(x.classes),reverse=True)

    def generate_table(self):
        self.sort_by_number_of_classes()
        url_list = []
        exists_list = []
        class_num_list = []
        id_num_list = []
        inline_list = []
        class_uses_list = []
        id_uses_list = []
        for stylesheet in self.sheets:
            url_list.append(stylesheet.url)
            exists_list.append(stylesheet.exists)
            inline_list.append(stylesheet.inline)
            class_num_list.append(len(stylesheet.classes))
            id_num_list.append(len(stylesheet.id_selectors))
            class_uses_list.append(stylesheet.class_uses)
            id_uses_list.append(stylesheet.id_uses)
            
        return generate_table(["File","Exists","Is Inline","Number of Classes","Number of IDs","Class Uses","Id Uses"],[url_list,exists_list,inline_list,class_num_list,id_num_list,class_uses_list,id_uses_list])

    def __repr__(self):
        string = ""
        for sheet in self.sheets:
            string += str(sheet)+'\n'
        return string

class NoDefinitionClasses:
    def __init__(self):
        self.list = []
    
    def add(self,name,file):
        for item in self.list:
            if item["name"] == name: #and item["file"] == file:
                return
        self.list.append({"name":name,"file":file})
    
    def generate_table(self):
        classname_list = []
        url_list = []
        for _class in self.list:
            classname_list.append(_class["name"])
            url_list.append(_class["file"])
        return generate_table(["Class Name","File"],[classname_list,url_list])


class AnalysisClass:
    def __init__(self,html_dir,markdown_dir,verbose,inline_styles):
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
        self.stylesheets = Stylesheets(self.classes,self.verbose)
        self.no_definition_classes = NoDefinitionClasses()
        self.inline_styles = inline_styles

    def start(self):
        cwd = os.getcwd()
        os.chdir(self.html_dir)
        html_files = glob("**/*.html",recursive=True)
        if self.verbose:
            print("Analyzing html files for class usage")
        for i,file in enumerate(html_files):
            if self.verbose:
                print(f" ({str(i+1).zfill(len(str(len(html_files))))}/{str(len(html_files))}) Analyzing '{file}'")
            self.analyze_file(file)
            #break
        #if self.verbose:
        #    print(self.stylesheets)
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
                        self.stylesheets.add(stylesheet)
            css_style = 1
            if self.inline_styles and "style" in tags:
                for style in soup.find_all("style"):
                    self.stylesheets.add(file+"_style_"+str(css_style),style.get_text())
                    css_style += 1
            for tag in tags:
                for i in soup.find_all(tag):
                    if i.has_attr("class") and len(i["class"]) != 0:
                        for j in i["class"]:
                            if not self.classes.update_uses(j):
                                self.no_definition_classes.add(j,file)
                    if i.has_attr("id") and len(i["id"]) != 0:
                        id = '#'+i["id"]
                        if not self.classes.update_uses(id):
                            self.no_definition_classes.add(id,file)

    def write_output(self):
        os.chdir(self.markdown_dir)
        if self.verbose:
            print("Writing class_usage.md")
        with open("class_usage.md","w") as f:
            f.write("# Class Usage\n")
            f.write(self.classes.generate_table_of_uses())
        if self.verbose:
            print("Writing not_defined_classes.md")
        with open("not_defined_classes.md","w") as f:
            f.write("# Classes With No Definitions in stylesheets\n## Note: Most of these are probably in css from outsite the site, or from errors in parsing classes\n")
            f.write(self.no_definition_classes.generate_table())
        if self.verbose:
            print("Writing stylesheets.md")
        with open("stylesheets.md","w") as f:
            f.write("# Stylesheets\n")
            f.write(self.stylesheets.generate_table())
    
