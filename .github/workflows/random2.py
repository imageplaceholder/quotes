"""
Create a function that creates a HTML index inside every folder and sub folder in a path. With option  to exclude folders by names and files by names.
"""

import os
import sys
import argparse
import shutil
import glob
import re

def create_index(path, exclude_folders, exclude_files):
    """
    Create a function that creates a HTML index inside every folder and sub folder in a path. With option  to exclude folders by names and files by names.
    """
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
    index_file.write("<head>\n")
    index_file.write("<title>Index of " + path + "</title>\n")
    index_file.write("</head>\n")
    index_file.write("<body>\n")
    index_file.write("<h1>Index of " + path + "</h1>\n")
    index_file.write("<hr>\n")
    index_file.write("<pre>\n")
    index_file.write("<a href=\"../\">../</a>\n")
    for folder in folders:
        dir_path = folder
        dir_size = os.path.getsize(dir_path)
        dir_last_modified = os.path.getmtime(dir_path)
        index_file.write('<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="' + dir + '">' + dir + '</a></td><td align="right">' + str(dir_last_modified) + '</td><td align="right">' + str(dir_size) + '</td><td>&nbsp;</td></tr>\n')
    for file in files:
        file_path = file
        file_size = os.path.getsize(file_path)
        file_last_modified = os.path.getmtime(file_path)
        index_file.write('<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="' + file + '">' + file + '</a></td><td align="right">' + str(file_last_modified) + '</td><td align="right">' + str(file_size) + '</td><td>&nbsp;</td></tr>\n')
    index_file.write("</pre>\n") 
    index_file.write("<hr>\n")
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
