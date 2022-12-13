"""
Create a function to get all download urls for all folders and files in a GitHub repo from GitHub api.
Create a function to seperate each folder name by object with the folder name & folder path download urls in JSON file.
"""

import requests
import json
from urllib.parse import urlparse

def get_download_url(url):
    """
    Get download url for all folders and files in a GitHub repo.
    """
    # Get download url for all folders and files in a GitHub repo.
    download_url_list = []
    # Get the repo name from the url.
    repo_name = urlparse(url).path.split('/')[-1]
    # Get the repo owner from the url.
    repo_owner = urlparse(url).path.split('/')[-2]
    # Get the repo url from the url.
    repo_url = url
    # Get the GitHub api url.
    api_url = 'https://api.github.com/repos/' + repo_owner + '/' + repo_name + '/contents'
    # Get the response from GitHub api.
    response = requests.get(api_url)
    # Get the response content.
    response_content = response.content
    # Get the response content in json format.
    response_content_json = json.loads(response_content)
    # Get the download url for each folder and file in the repo.
    for item in response_content_json:
        # If the item is a folder.
        if item['type'] == 'dir':
            # Get the folder name.
            folder_name = item['name']
            # Get the folder path.
            folder_path = item['path']
            # Get the download url for the folder.
            folder_download_url = item['download_url']
            # Add the folder download url to the download url list.
            download_url_list.append(folder_download_url)
            # Get the GitHub api url for the folder.
            folder_api_url = 'https://api.github.com/repos/' + repo_owner + '/' + repo_name + '/contents/' + folder_path
            # Get the response from GitHub api for the folder.
            folder_response = requests.get(folder_api_url)
            # Get the response content for the folder.
            folder_response_content = folder_response.content
            # Get the response content in json format for the folder.
            folder_response_content_json = json.loads(folder_response_content)
            # Get the download url for each file in the folder.
            for folder_item in folder_response_content_json:
                # If the item is a file.
                if folder_item['type'] == 'file':
                    # Get the file name.
                    file_name = folder_item['name']
                    # Get the file path.
                    file_path = folder_item['path']
                    # Get the download url for the file.
                    file_download_url = folder_item['download_url']
                    # Add the file download url to the download url list.
                    download_url_list.append(file_download_url)
        # If the item is a file.
        elif item['type'] == 'file':
            # Get the file name.
            file_name = item['name']
            # Get the file path.
            file_path = item['path']
            # Get the download url for the file.
            file_download_url = item['download_url']
            # Add the file download url to the download url list.
            download_url_list.append(file_download_url)
    return download_url_list

def seperate_by_folder(url):
    """
    Seperate each folder name by object with the folder name & folder path download urls in JSON file.
    """
    # Get download url for all folders and files in a GitHub repo.
    download_url_list = get_download_url(url)
    # Get the repo name from the url.
    repo_name = urlparse(url).path.split('/')[-1]
    # Get the repo owner from the url.
    repo_owner = urlparse(url).path.split('/')[-2]
    # Get the repo url from the url.
    repo_url = ""
    # Get the GitHub api url.
    api_url = 'https://api.github.com/repos/' + repo_owner + '/' + repo_name + '/contents'
    # Get the response from GitHub api.
    response = requests.get(api_url)
    # Get the response content.
    response_content = response.content
    # Get the response content in json format.
    response_content_json = json.loads(response_content)
    # Create a list to store the folder name.
    folder_name_list = []
    # Get the folder name for each folder in the repo.
    for item in response_content_json:
        # If the item is a folder.
        if item['type'] == 'dir':
            # Get the folder name.
            folder_name = item['name']
            # Add the folder name to the folder name list.
            folder_name_list.append(folder_name)
    # Create a dictionary to store the folder name & folder path download urls.
    folder_download_url_dict = {}
    # Get the folder name & folder path download urls for each folder in the repo.
    for folder_name in folder_name_list:
        # Create a list to store the folder path download urls.
        folder_path_download_url_list = []
        # Get the folder path download urls for each folder in the repo.
        for download_url in download_url_list:
            # If the download url is a folder path download url.
            if folder_name in download_url:
                # Add the folder path download url to the folder path download url list.
                folder_path_download_url_list.append(download_url)
        # Add the folder name & folder path download urls to the folder download url dictionary.
        folder_download_url_dict[folder_name] = folder_path_download_url_list
    # Write the folder download url dictionary to a JSON file.
    with open('folder_download_urls.json', 'w') as outfile:
        json.dump(folder_download_url_dict, outfile)

if __name__ == '__main__':
    # Get download url for all folders and files in a GitHub repo.
    download_url_list = get_download_url('https://github.com/hupili/python-for-data-and-media-communication-gitbook')
    # print(download_url_list)
    # Seperate each folder name by object with the folder name & folder path download urls in JSON file.
    seperate_by_folder(download_url_list)
