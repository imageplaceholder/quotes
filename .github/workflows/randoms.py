"""
1. Create a function to make a HTML index of all files in a folder & sub folder.
"""

import os

def make_index(folder):
    """
    Create a HTML index of all files in a folder & sub folder.
    """
    index = open(os.path.join(folder, 'index.html'), 'w')
    index.write('<html><body>\n')
    
    for f in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, f)):
            index.write("<li><a href='{}/index.html'>{}</a></li>".format(f, f))
        else:
            if f != 'index.html': 
               index.write("<li><a href='{}'>{}</a></li>".format(f, f))
            
   # for root, dirs, files in os.walk(folder):
       # for file in files:
            #if file != 'index.html':
              #  if os.path.isdir(os.path.join(root, file)):
             #       index.write('<a href="{}">{}</a><br>\n'.format(os.path.join(root, file), file))
    index.write('</body></html>\n')
    index.close()

##make_index('./')



def create_index_for_sub_folder(path):
    """
    For every sub folder in a folder, if sub folder name is not in list. Create and write out a index file inside sub folder.
    """
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            if f not in ["a", "b", "c"]:
                with open(os.path.join(path, f, "index.html"), "w") as fp:
                    fp.write(make_index(os.path.join(path, f)))

create_index_for_sub_folder("./")
