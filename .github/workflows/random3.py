"""
Create a function to get all raw file content paths for a GitHub repo from GitHub api.
Create a function to seperate all file contents paths by directory name and parent paths in JSON file.
"""

import requests
import json

def get_file_content_paths(repo_owner, repo_name):
    """
    Get all raw file content paths for a GitHub repo from GitHub api.
    """
    # Get all raw file content paths for a GitHub repo from GitHub api.
    url = 'https://api.github.com/repos/' + repo_owner + '/' + repo_name + '/contents'
    response = requests.get(url)
    file_content_paths = json.loads(response.text)
    return file_content_paths

def seperate_file_content_paths(file_content_paths):
    """
    Seperate all file contents paths by directory name and parent paths in JSON file.
    """
    # Seperate all file contents paths by directory name and parent paths in JSON file.
    file_content_paths_by_dir = {}
    for file_content_path in file_content_paths:
        if file_content_path['type'] == 'dir':
            file_content_paths_by_dir[file_content_path['name']] = []
            file_content_paths_by_dir[file_content_path['name']].append(file_content_path['path'])
        else:
            file_content_paths_by_dir[file_content_path['name']] = []
            file_content_paths_by_dir[file_content_path['name']].append(file_content_path['path'])
    return file_content_paths_by_dir

def main():
    """
    Main function.
    """
    # Get all raw file content paths for a GitHub repo from GitHub api.
    file_content_paths = get_file_content_paths('YaleDHLab', 'lab-workshops')

    # Seperate all file contents paths by directory name and parent paths in JSON file.
    file_content_paths_by_dir = seperate_file_content_paths(file_content_paths)
    with open('file_content_paths_by_dir.json', 'w') as outfile:
        json.dump(file_content_paths_by_dir, outfile)

if __name__ == '__main__':
    main()
