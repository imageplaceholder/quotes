"""
Create a function to get all download urls for all folders and sub folders in a GitHub repo from GitHub api. Seperate each folder name by object with the folder name & all the download urls inside folder. Then save to JSON file.
"""

import requests
import json
import os
import re

def get_download_urls(repo_url):
    """
    Get all download urls for all folders and sub folders in a GitHub repo from GitHub api. Seperate each folder name by object with the folder name & all the download urls inside folder. Then save to JSON file.
    """

    # Get the repo name from the url
    repo_name = re.search(r'github.com/(.*)', repo_url).group(1)

    # Get the repo content from GitHub api
    repo_content = requests.get('https://api.github.com/repos/{}/contents'.format(repo_name)).json()

    # Create a dictionary to store the folder name & download urls
    download_urls = {}

    # Loop through all the files and folders in the repo
    for item in repo_content:
        # If the item is a folder
        if item['type'] == 'dir':
            # Get the folder name
            folder_name = item['name']

            # Get the folder content from GitHub api
            folder_content = requests.get(item['url']).json()

            # Create a list to store the download urls
            urls = []

            # Loop through all the files and folders in the folder
            for file in folder_content:
                # If the item is a file
                if file['type'] == 'file':
                    # Get the download url
                    url = file['download_url']

                    # Add the download url to the list
                    urls.append(url)

            # Add the folder name & download urls to the dictionary
            download_urls[folder_name] = urls

    # Save the dictionary to a JSON file
    with open('download_urls.json', 'w') as f:
        json.dump(download_urls, f, indent=4)

if __name__ == '__main__':
    get_download_urls('https://github.com/jhu-ep-coursera/fullstack-course4')
