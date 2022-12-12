## Project: Create a function to make a HTML index of all files in a folder & sub-folders (optional). So it can be used to directory list all files on a static
## website like GitHub Pages. 

### To do 
# get modified dates
# get all files in sub / sub folders. 
# icons for file types 
# add go back to parent directory in HTML for sub folders.
# add breadcrumbs to show where in directory you are. 
# add way to exclude files from directory listing.
# add way to exclude folders from directory listing. 
# improve / fix proper usage of checking if folder.
# avoid all .github related folder (.git / .github etc..)
# use jinja template for easier customization. 
# make function to make a single index in a single folder. (ie; do not add index.html to folder files.)

### Javascript To Do
## Click to sort. 
## Possibily a search feature bar.




import os

def make_index(folder):
    """
    Create a HTML index of all files in a folder.
    """
    
   # if os.path.dirname(folder) in ["git", "github"]:
    #    return
        
    index = open(os.path.join(folder, 'index.html'), 'w')
    index.write('<html><body>\n')
    
    Directories = ""
    Files = ""
    print(os.path.dirname(folder))
    for f in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, f)):
            if f not in [".git", ".github"]:
                Directories += "<li><a href='{}/index.html'>{}</a></li>".format(f, f)
        else:
            if f != 'index.html': 
               Files += "<li><a href='{}'>{}</a></li>".format(f, f)
               #index.write("<li><a href='{}'>{}</a></li>".format(f, f))
            
    index.write(Directories + Files + '</body></html>\n')
    index.close()





def create_index_for_sub_folder(path):
    """
    Function to create index file for every sub folder inside of a path.
    """
    make_index(path)
    for f in os.listdir(path):
        print(path)
        if os.path.isdir(os.path.join(path, f)):
            if f not in ["git", "github", ".github"]:
                make_index(os.path.join(path, f))

                
## pass the path to make HTML index directorys for                
create_index_for_sub_folder("./")
