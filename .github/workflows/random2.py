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

## Check if parent directory. 
FirstFolderProcessed = False






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
    return datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')


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
    print(FirstFolderProcessed)
    for folder in folders:
        dir_path = os.path.join(path, folder)
        print(dir_path)
        dir_size = readable_size(os.path.getsize(dir_path))
        dir_last_modified = mtime_to_timestamp(str(os.path.getmtime(dir_path)))
        folder_string = '<tr><td valign="top"><span class="fiv-cla fiv-icon-folder"></span></td><td><a href="' + folder + '">' + folder + '</a></td><td align="right">' + str(dir_last_modified) + '</td><td align="right">' + str(dir_size) + '</td><td>&nbsp;</td></tr>\n'
        index_file.write(folder_string)
        FirstFolderProcessed = True
    for file in files:
        file_path = os.path.join(path, file)
        print(file_path + "file")
        file_size = readable_size(os.path.getsize(file_path))
        file_last_modified = mtime_to_timestamp(str(os.path.getmtime(file_path)))
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
