"""
Create a function that creates a JSON file with every download url for all folders and sub folders in a Github repo from GitHub API. Seperate each folder name by object with the folder name with all the download urls. With option to exclude folders or files by names.
"""

import requests
import json
import os
import sys
import argparse

def get_repo_info(repo_name):
    """
    Get the repo info from the GitHub API.
    """
    url = "https://api.github.com/repos/{}/contents".format(repo_name)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: {}".format(response.status_code))
        sys.exit(1)

def get_download_url(repo_name, file_name):
    """
    Get the download url for a file from the GitHub API.
    """
    url = "https://api.github.com/repos/{}/contents/{}".format(repo_name, file_name)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["download_url"]
    else:
        print("Error: {}".format(response.status_code))
        sys.exit(1)

def get_download_urls(repo_name, repo_info, exclude_folders=[], exclude_files=[]):
    """
    Get the download urls for all files in a repo.
    """
    download_urls = {}
    for item in repo_info:
        print(repo_info[item])
        if repo_info[item]["type"] == "dir":
            if repo_info[item]["name"] not in exclude_folders:
                download_urls[repo_info[item]["name"]] = get_download_urls(repo_name, repo_info[item]["_links"]["self"], exclude_folders, exclude_files)
        elif repo_info[item]["type"] == "file":
            if repo_info[item]["name"] not in exclude_files:
                download_urls[item["name"]] = get_download_url(repo_name, repo_info[item]["path"])
    return download_urls

def main():
    """
    Main function.
    """
    #parser = argparse.ArgumentParser(description="Create a JSON file with all download urls for all folders and sub folders in a Github repo from GitHub API.")
    #parser.add_argument("repo_name", help="The name of the repo.")
    #parser.add_argument("-o", "--output", help="The name of the output file.")
    #parser.add_argument("-e", "--exclude", help="The name of the file with the folders and files to exclude.")
   # args = parser.parse_args()

    #repo_name = args.repo_name
    #output_file = args.output
    #exclude_file = args.exclude
    repo_name = "imageplaceholder/quotes"
    output_file = "test.json"
    exclude_file = []
    exclude_folders = []
    exclude_files = []
    if exclude_file:
        with open(exclude_file, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                if line.startswith("folder:"):
                    exclude_folders.append(line.split(":")[1].strip())
                elif line.startswith("file:"):
                    exclude_files.append(line.split(":")[1].strip())

    repo_info = get_repo_info(repo_name)
    download_urls = get_download_urls(repo_name, repo_info, exclude_folders, exclude_files)

    if output_file:
        with open(output_file, "w") as f:
            json.dump(download_urls, f, indent=4)
    else:
        print(json.dumps(download_urls, indent=4))

if __name__ == "__main__":
    main()
