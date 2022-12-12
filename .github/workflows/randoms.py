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

## make some icons to be includes by converting png etc to base 64 and making basic style sheet like so 
""" CSS example 

span.swf
{
	background:
	 url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAjZJREFUeNqMUk1rE1EUPfORptFEDNhgBaGQXQv+hC5m14Ibl0K3jVkUSgNuii0FF3WhCxclq4KF0G23pRi6KFhUZIKIQoWClkIpIbEYJ+l8ee7rmzELER+ceW/u3HPuvWee8R7A+soKDMO4z+M4/r2aURR9jcIQcRzjy8EBDBH4NjGBxtxcZWt1tX7Jj74gihAySRJlua6Lrb29R0okDI+SuPEBeH4NWLLkhQiJgPCJS8Jid9lKBa1WCw9nZvBgebnK8GsKHCmBT0B8g4csYWpin/CIHvGLuHV6imazmc7xstF4wu2pnO1gqKp0MDo/j9v1ukr87Di42N+HbZpweJa2C4UCdl23k4iZgW61r3Gd7XY3N+GS1CZZOhqxbSVCoxUpCEODkB32gIGMzCrVJyeRKZdxk7jj+/hYrSrx0UzmqlwQKJEwCIykA7uvWx/J5zG+sICw3cYbCgy0D6qAZaXzW1cCZirgaePura2hODuL440N/NSxxFCTpETE4h4MCwx0lbe1GkDE2tSIiLU/pp5dRCx6EQyPwIQXNHIp0qRoiCwoLy6mAukIvv+nAybXjkul2o7jPH63vf2MV1URI30LZZdYsgzl5dAIu2NjcKenJarqSDUhqV1fLrBtaBGJJyP0zs9hv+Lj7skJcsWirSowwdQd/E1EmF6vZ3udDr4fHqpvOR5KPzqdbNqmiJAgAmKawKaBNi+U/AXJFY5wpWqOKF2cnXXzU1Pr+I8VeV5XOGLHbwEGAJZPA5r+wu15AAAAAElFTkSuQmCC')
	no-repeat
	left center !important;
	padding: 0px 0px 0px 25px;
}

""""

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
