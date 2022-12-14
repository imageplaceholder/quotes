"""
Create a function that creates a JSON file with all folders and files of a GitHub repo represented in a tree directory format with parent folder URL included. 
"""

import requests
import json

def get_repo_tree(repo_url):
    """
    Create a function that creates a JSON file with all folders and files of a GitHub repo represented in a tree directory format with parent folder URL included. 
    """
    # get the repo name from the url
    repo_name = repo_url.split('/')[-1]
    # get the repo owner from the url
    repo_owner = repo_url.split('/')[-2]
    # get the repo tree
    repo_tree = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/master?recursive=1').json()
    # create a list to store the tree
    tree = []
    # loop through the tree
    for item in repo_tree['tree']:
        # if the item is a folder
        if item['type'] == 'tree':
            # add the folder to the tree
            tree.append({'name': item['path'], 'url': item['url'], 'type': item['type']})
        # if the item is a file
        elif item['type'] == 'blob':
            # add the file to the tree
            tree.append({'name': item['path'], 'url': item['url'], 'type': item['type']})
    # create a list to store the tree
    tree_list = []
    # loop through the tree
    for item in tree:
        # if the item is a folder
        if item['type'] == 'tree':
            # get the folder name
            folder_name = item['name']
            # get the folder url
            folder_url = item['url']
            # get the folder path
            folder_path = folder_name.split('/')
            # create a list to store the folder path
            folder_path_list = []
            # loop through the folder path
            for folder in folder_path:
                # add the folder to the folder path list
                folder_path_list.append(folder)
                # if the folder path list is not empty
                if folder_path_list:
                    # get the parent folder name
                    parent_folder_name = '/'.join(folder_path_list[:-1])
                    # get the parent folder url
                    parent_folder_url = [folder['url'] for folder in tree if folder['name'] == parent_folder_name][0]
                    # add the folder to the tree list
                    tree_list.append({'name': folder, 'url': folder_url, 'parent_folder_name': parent_folder_name, 'parent_folder_url': parent_folder_url, 'type': item['type']})
        # if the item is a file
        elif item['type'] == 'blob':
            # get the file name
            file_name = item['name']
            # get the file url
            file_url = item['url']
            # get the file path
            file_path = file_name.split('/')
            # create a list to store the file path
            file_path_list = []
            # loop through the file path
            for file in file_path:
                # add the file to the file path list
                file_path_list.append(file)
                # if the file path list is not empty
                if file_path_list:
                    # get the parent folder name
                    parent_folder_name = '/'.join(file_path_list[:-1])
                    # get the parent folder url
                    parent_folder_url = [folder['url'] for folder in tree if folder['name'] == parent_folder_name][0]
                    # add the file to the tree list
                    tree_list.append({'name': file, 'url': file_url, 'parent_folder_name': parent_folder_name, 'parent_folder_url': parent_folder_url, 'type': item['type']})
    # create a json file with the tree list
    with open(f'{repo_name}_tree.json', 'w') as f:
        json.dump(tree_list, f, indent=4)

# get the repo url
repo_url = "https://github.com/imageplaceholder/quotes/"
# get the repo tree
get_repo_tree(repo_url)
