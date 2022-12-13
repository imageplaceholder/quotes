"""
Create a function that creates a JSON file with file paths of every folder and sub folder in a path with a JSON key in each file for pagination. With option  to exclude folders by names and files by names.
"""

import os
import json
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Create a JSON file with file paths of every folder and sub folder in a path with a JSON key in each file for pagination. With option  to exclude folders by names and files by names.')
    parser.add_argument('-p', '--path', help='Path to the folder', required=True)
    parser.add_argument('-e', '--exclude', help='Exclude folders by name', nargs='+')
    parser.add_argument('-f', '--files', help='Exclude files by name', nargs='+')
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    args = parser.parse_args()
    return args

def get_files(path, exclude, files):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".html"):
                if exclude:
                    if not any(x in root for x in exclude):
                        if files:
                            if not any(x in file for x in files):
                                files_list.append(os.path.join(root, file))
                        else:
                            files_list.append(os.path.join(root, file))
                else:
                    if files:
                        if not any(x in file for x in files):
                            files_list.append(os.path.join(root, file))
                    else:
                        files_list.append(os.path.join(root, file))
    return files_list

def create_json(files_list, output):
    json_data = {}
    for file in files_list:
        json_data[file] = {}
        json_data[file]['pagination'] = {}
        json_data[file]['pagination']['next'] = ''
        json_data[file]['pagination']['previous'] = ''
    with open(output, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

def main():
   # args = get_args()
    #files_list = get_files(args.path, args.exclude, args.files)
   # files_lists = "./", [".github"], None
    output = "./"
    #create_json(files_list, output)
    create_json(get_files("./", [".github"], None), "./")
if __name__ == '__main__':
    main()
