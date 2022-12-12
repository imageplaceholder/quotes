"""
1. Create a class to generate a HTML index of a website, with option to exclude file names and folders.  
"""

import os
import sys
import argparse

class IndexGenerator:
    def __init__(self, path, exclude_files, exclude_folders):
        self.path = path
        self.exclude_files = exclude_files
        self.exclude_folders = exclude_folders
        self.index_file = os.path.join(self.path, 'index.html')
        self.index_file_content = ''
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
        with open(self.index_file, 'w') as f:
            f.write(self.index_file_content)

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Generate a HTML index of a website, with option to exclude file names and folders.')
    #parser.add_argument('-p', '--path', help='Path to the website', required=True)
    #parser.add_argument('-ef', '--exclude_files', help='File names to exclude', nargs='+')
   # parser.add_argument('-efd', '--exclude_folders', help='Folder names to exclude', nargs='+')
  #  args = parser.parse_args()
    index_generator = IndexGenerator("./", "", [".github", "github"])
    index_generator.generate_index()
