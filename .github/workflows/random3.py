"""
Create a function that writes a JSON file of every file, folder and sub folder in a path. Store each folder name in each object wrote. With option  to exclude folders by names and files by names.
"""

import os
import json

def write_json(path, exclude_folders=[], exclude_files=[]):
    """
    Write a JSON file of every file, folder and sub folder in a path. Store each folder name in each object wrote. With option  to exclude folders by names and files by names.
    """
    json_file = {}
    for root, dirs, files in os.walk(path):
        for folder in dirs:
            if folder not in exclude_folders:
                json_file[folder] = {}
                for root_2, dirs_2, files_2 in os.walk(os.path.join(root, folder)):
                    for file in files_2:
                        if file not in exclude_files:
                            json_file[folder][file] = {}
    with open(os.path.join(path, 'json_file.json'), 'w') as f:
        json.dump(json_file, f, indent=4)

if __name__ == '__main__':
    write_json('./', exclude_folders=['.github/'], exclude_files=['file_1.txt', 'file_2.txt'])
