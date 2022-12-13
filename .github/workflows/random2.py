"""
Create a function that creates a HTML index inside every folder and sub folder in a path. With option  to exclude folders by names and files by names.
"""

import os
import sys
import argparse
import shutil
import glob
import re
import time
import datetime
import subprocess
import jinja2

## Check if parent directory. 
FirstFolderProcessed = False





"""
Create a function to write out a jinja template.
"""



def write_template(template_file, output_file):
    """
    Write out a jinja template.
    """
    # Load the template
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(template_file))
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(os.path.basename(template_file))
    
    test = """<tr>
    <td>
        <p style="display: none">openwrt-rockchip-armv8-friendlyarm_nanopi-r4s-ext4-sysupgrade.img.gz</p><img style="margin-right: 5px; max-width: 20px" src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAgJAAAICQBcEDPXgAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAARvSURBVGiB7ZlPaBxVHMc/b/7tzv5JskmaTVZt02LTJGpSakFQsGpFe6h6KChFiuJNquBFD0IRVOyp0ojgQQ+i9iBVohZB8GCx1EL/0CbUlhYbNW1j/plNNpndmd3542GbcUtz6frGveQ7h3nz3sz7/r7z+733fm8GVtFYiOXCodGXM66rDQnYHAiUejrzKr6wrYqaNtr1LZ27cgBfn3j/L4CWrFnWNIV4UvdUXQnqMjbA9wnO6pr32vMDH+UBtOVG2wmGyn5+T9mz6+kbALfsUbJcAl8lobQCMJOfWA/gJxNouoIpNDRDrZvDUOP3+X4a4IWbBBTsmS0upbo7Bqi4Ho7rMlMY58jIBwAM5nYAMBEcx3EtFFfDV+sXUPaKONj3L1+HoWI7lrbyI7cPp1Jk9MpxRq8cJ2v0kzX60dWErO4pOUuhrWHBp66wXBGJWBPbBp4AYDx/CoCyVqS+kXUram2V9tZrkYpneHDDswDs/2Y3AGvuSqIZkhTUIBIBjlvk2sIFAO7I3A2AJ2YBTzpXJAIWrBk+/+kdAJ7p2QfAef8QxWBGOlckAhShYMaSACzPbL7v1aw68iBVgBBVC+PxBC/uOIAi1HAMdK5PIYRAKHJVSB1VqiYQojpXn7j+BRXfQQho6YgjlGqbqsoVINcDisAwNZJ00JPbSqrF4K09h7g2f4Fffv+KItPSPSB9DKxr7+OpjfvQlXhYl0nk2JR9iCO/vcuUdVkqn9QQUoTK9u5X0ZU4s9Y4w2cOMHzmALPWOIZq8nj3Kwghdy2Q6oFssofmWCeuV+HjH99gsTQHwKWrp3n96c9ojnWRTW5kcumSNE6pryOltwFQKM1iOXnSrTHSrTGWnDkWin8DkNbXyKSU6wHfrZ5bkll6e/soeNcBWNu5kUyy46Z7ZEGqAM+tJlmKUNh1z9uMTn8PwGDHzjD2fU9e0giyZ6HgX+NMrYkHcrtvvcWXK0B+eliDYmWeYmU+SopociGAH859wrGLhwF4uP85nhx8KRKeSDywZOc5dvEwwY3j5wtfYtnReCISDyzaeRLNOk3t1dW4MGtTsOdIxlukc0UiQAAtWZMbyWm1HAURkkPICyoAmLF0aDyAENV9MoDrl2VSyhUwtTgGQLO5hk2t28L63rZHaTLbCQiYWroik1JuCM3bk4z+eZSBdY+wvXsvfW2PAZBL9wEw+sdRCs40pqFL45QqQDcUhk8eJG6k6OnaSi7dH7ZdmjjJ8KmDZO6s/6PWSpArIK6CbvPp0TfZkB2kZ+1mCODytXOMTY4QMzX0mCGTUv4s1NplMnPVYmxqhLGpkbBeN1Rau0zZdPIFqLpCtjuFtVDBKVVTz5ipkWzWpW8nIap1QBGkMgapjNxwWQmRJnP/B1YFNBqrAhqNVQGNxqqARiMUIKL4/xMRam0NBZQWK+caY87to1hwzy6Xw1zo26Ff9+/c268l0sa9KEFUW9j/Bl8E1kL5/HcfXnxvuarWUA1YC6SJ5G+WFATAIjAOSP7K2iD8A6+nWFo67ZFWAAAAAElFTkSuQmCC"><a href="openwrt-rockchip-armv8-friendlyarm_nanopi-r4s-ext4-sysupgrade.img.gz">openwrt-rockchip-armv8-friendlyarm_nanopi-r4s-ext4-sysupgrade.img.gz</a>
    </td>
    <td>11496 kB</td>
    <td>06-Aug-2021 19:37</td>
</tr>"""

    # Write out the template
    with open(output_file, 'w') as f:
        f.write(template.render(GEN_DIRS = test))


write_template(".github/workflows/template.html", "./test.html")

def readable_size(size):
    """
    Convert file size to human readable format.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']:
        if abs(size) < 1024.0:
            return "%3.1f %s" % (size, unit)
        size /= 1024.0
    return "%.1f %s" % (size, 'YB')




def mtime_to_timestamp(mtime):
    """
    Convert mtime to timestamp.
    """
    return datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')





def convert_timestamp(timestamp):
    """
    Convert timestamp to integer.
    """
    return int(datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z').timestamp())



def is_github():
    """
    function to detect if running on GitHub.
    """
    return os.environ.get('GITHUB_ACTIONS', None) is not None



## Function to get File Creation Dates (GitHub)
def lastmod_github(f) :
    """
    function to get file mod dates for Github!
    f - filename
    
    -1 returns last Commit For Git Log 
   --reverse returns First Commit
    """
    mod = subprocess.run(['git', 'log', '-1', '--format=%cI', f],
                    stdout=subprocess.PIPE,
                    universal_newlines=True).stdout.strip()
    if len(mod) == 0 :
        mod = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    return mod





def create_index(path, exclude_folders, exclude_files):
    """
                      self.index_file_content += '<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="' + file + '">' + file + '</a></td><td align="right">' + str(file_last_modified) + '</td><td align="right">' + str(file_size) + '</td><td>&nbsp;</td></tr>\n'
            for dir in dirs:
                if dir not in self.exclude_folders:
                    dir_path = os.path.join(root, dir)
                    dir_size = os.path.getsize(dir_path)
                    dir_last_modified = os.path.getmtime(dir_path)
                    self.index_file_content += '<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="' + dir + '">' + dir + '</a></td><td align="right">' + str(dir_last_modified) + '</td><td align="right">' + str(dir_size) + '</td><td>&nbsp;</td></tr>\n'
    Create a function that creates a HTML index inside every folder and sub folder in a path. With option  to exclude folders by names and files by names.
    
    
    
    
      self.index_file_content += '<html>\n'
        self.index_file_content += '<head>\n'
        self.index_file_content += '<title>Index of ' + self.path + '</title>\n'
        self.index_file_content += '</head>\n'
        self.index_file_content += '<body>\n'
        self.index_file_content += '<h1>Index of ' + self.path + '</h1>\n'
        self.index_file_content += '<table>\n'
        self.index_file_content += '<tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>\n'
        self.index_file_content += '<tr><th colspan="5"><hr></th></tr>\n'
        self.index_file_content += '<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>\n'
        self.index_file_content += '<tr><th colspan="5"><hr></th></tr>\n'
    def generate_index(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file not in self.exclude_files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    file_last_modified = os.path.getmtime(file_path)
                    self.index_file_content += '<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="' + file + '">' + file + '</a></td><td align="right">' + str(file_last_modified) + '</td><td align="right">' + str(file_size) + '</td><td>&nbsp;</td></tr>\n'
            for dir in dirs:
                if dir not in self.exclude_folders:
                    dir_path = os.path.join(root, dir)
                    dir_size = os.path.getsize(dir_path)
                    dir_last_modified = os.path.getmtime(dir_path)
                    self.index_file_content += '<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="' + dir + '">' + dir + '</a></td><td align="right">' + str(dir_last_modified) + '</td><td align="right">' + str(dir_size) + '</td><td>&nbsp;</td></tr>\n'
        self.index_file_content += '</table>\n'
        self.index_file_content += '</body>\n'
        self.index_file_content += '</html>\n'
    """
    # Add parent directory link 
    global FirstFolderProcessed
    
    # Get all folders in path
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    # Remove excluded folders
    folders = [f for f in folders if f not in exclude_folders]
    # Get all files in path
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    # Remove excluded files
    files = [f for f in files if f not in exclude_files]
    # Create index file
    index_file = open(os.path.join(path, "index.html"), "w")
    index_file.write("<html>\n")
    index_file.write('<head> <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/file-icon-vectors@1.0.0/dist/file-icon-vectors.min.css" /> \n' )
    index_file.write("<title>Index of " + path + "</title>\n")
    index_file.write("</head>\n")
    index_file.write("<body>\n")
    index_file.write("<h1>Index of " + path + "</h1>\n")
    index_file.write('<table><tr><th valign="top"><span></span></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>\n <tr><th colspan="5"><hr></th></tr>\n')
    if FirstFolderProcessed is True:
        index_file.write('<tr><td valign="top"><span class="fiv-cla fiv-icon-folder"></span></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>\n <tr><th colspan="5"><hr></th></tr>\n')
    print(is_github())
    for folder in folders:
        dir_path = os.path.join(path, folder)
        print(dir_path)
        dir_size = readable_size(os.path.getsize(dir_path))
        if is_github() is True:
            dir_last_modified = mtime_to_timestamp(convert_timestamp(lastmod_github(dir_path)))
        else:
            dir_last_modified = mtime_to_timestamp(os.path.getmtime(dir_path))
        folder_string = '<tr><td valign="top"><span class="fiv-cla fiv-icon-folder"></span></td><td><a href="' + folder + '">' + folder + '</a></td><td align="right">' + str(dir_last_modified) + '</td><td align="right">' + str(dir_size) + '</td><td>&nbsp;</td></tr>\n'
        index_file.write(folder_string)
        FirstFolderProcessed = True
    for file in files:
        file_path = os.path.join(path, file)
        print(file_path + "file")
        file_size = readable_size(os.path.getsize(file_path))
        if is_github() is True:
            file_last_modified = mtime_to_timestamp(convert_timestamp(lastmod_github(file_path)))
        else:
            file_last_modified = mtime_to_timestamp(os.path.getmtime(file_path))
        file_ext = file.split(".")[-1]
        file_string = f'<tr><td valign="top"><span class="fiv-cla fiv-icon-{file_ext}"></span></td><td><a href="' + file + '">' + file + '</a></td><td align="right">' + str(file_last_modified) + '</td><td align="right">' + str(file_size) + '</td><td>&nbsp;</td></tr>\n'
        index_file.write(file_string)
        FirstFolderProcessed = True
    index_file.write('</table>\n')
    index_file.write("</body>\n")
    index_file.write("</html>\n")
    index_file.close()
    # Create index in sub folders
    for folder in folders:
        create_index(os.path.join(path, folder), exclude_folders, exclude_files)

def main():
    """
    Main function
    """
    # Create the parser
  #  my_parser = argparse.ArgumentParser(description='Create a function that creates a HTML index inside every folder and sub folder in a path. With option  to exclude folders by names and files by names.')
    # Add the arguments
 #   my_parser.add_argument('Path',
          #                 metavar='path',
         #                  type=str,
        #                   help='the path to create the index')
  #  my_parser.add_argument('-e',
   #                        '--exclude',
    #                       metavar='exclude',
     #                      type=str,
      #                     nargs='+',
       #                    help='exclude folders and files')
    # Execute the parse_args() method
 #   args = my_parser.parse_args()
    path = "./"
    exclude = [".github", ".git"]
    exclude_folders = []
    exclude_files = ["index.html"]
    if exclude:
        for item in exclude:
            if os.path.isdir(os.path.join(path, item)):
                exclude_folders.append(item)
            elif os.path.isfile(os.path.join(path, item)):
                exclude_files.append(item)
    create_index(path, exclude_folders, exclude_files)

if __name__ == "__main__":
    main()
