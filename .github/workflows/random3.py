"""
Write a JSON list of all contents inside every folder and sub folder in a path. Grouped by folder path. With option to exclude folders and files from list.
"""

import os
import json
import argparse

#parser = argparse.ArgumentParser(description='Write a JSON list of all contents inside every folder and sub folder in a path. Grouped by folder path. With option to exclude folders and files from list.')
#parser.add_argument('path', help='Path to folder to list')
#parser.add_argument('-e', '--exclude', nargs='+', help='List of folders and files to exclude from list')
#parser.add_argument('-o', '--output', help='Output file name')
#args = parser.parse_args()

#path = args.path
#exclude = args.exclude
output = ""

if not output:
    output = 'list.json'

def list_files(path, exclude):
    files = []
    for file in os.listdir(path):
        if file not in exclude:
            files.append(file)
    return files

def list_folders(path, exclude):
    folders = []
    for folder in os.listdir(path):
        if folder not in exclude:
            folders.append(folder)
    return folders

def list_path(path, exclude):
    files = list_files(path, exclude)
    folders = list_folders(path, exclude)
    return {
        'files': files,
        'folders': folders
    }

def list_path_recursive(path, exclude):
    files = list_files(path, exclude)
    folders = list_folders(path, exclude)
    subfolders = {}
    for folder in folders:
        subfolders[folder] = list_path_recursive(path + '/' + folder, exclude)
    return {
        'files': files,
        'folders': subfolders
    }

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

write_json("/", list_path_recursive("/", ["git", "github"]))
