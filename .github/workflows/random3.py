""" 
Create a class to write a JSON file of all files and folders (including sub folders) download_urls from a GitHub repo with option to exclude file names and folders.
"""

import os
import json
import requests
import argparse

class GitHubRepoDownloader:
    def __init__(self, repo_url, exclude_file_names=None, exclude_folders=None):
        self.repo_url = repo_url
        self.exclude_file_names = exclude_file_names
        self.exclude_folders = exclude_folders
        self.repo_name = self.repo_url.split('/')[-1]
        self.repo_owner = self.repo_url.split('/')[-2]
        self.repo_contents_url = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents'
        self.repo_contents = self.get_repo_contents()
        self.repo_download_urls = self.get_repo_download_urls()
        self.repo_download_urls_json = self.get_repo_download_urls_json()
        self.write_repo_download_urls_json()

    def get_repo_contents(self):
        repo_contents = requests.get(self.repo_contents_url).json()
        return repo_contents

    def get_repo_download_urls(self):
        repo_download_urls = []
        for repo_content in self.repo_contents:
            print(repo_content)
            if repo_content['type'] == 'file':
                if self.exclude_file_names:
                    if repo_content['name'] not in self.exclude_file_names:
                        repo_download_urls.append(repo_content['download_url'])
                else:
                    repo_download_urls.append(repo_content['download_url'])
            elif repo_content['type'] == 'dir':
                if self.exclude_folders:
                    if repo_content['name'] not in self.exclude_folders:
                        repo_download_urls.extend(self.get_repo_download_urls_from_folder(repo_content['url']))
                else:
                    repo_download_urls.extend(self.get_repo_download_urls_from_folder(repo_content['url']))
        return repo_download_urls

    def get_repo_download_urls_from_folder(self, folder_url):
        folder_contents = requests.get(folder_url).json()
        folder_download_urls = []
        for folder_content in folder_contents:
            if folder_content['type'] == 'file':
                if self.exclude_file_names:
                    if folder_content['name'] not in self.exclude_file_names:
                        folder_download_urls.append(folder_content['download_url'])
                else:
                    folder_download_urls.append(folder_content['download_url'])
            elif folder_content['type'] == 'dir':
                if self.exclude_folders:
                    if folder_content['name'] not in self.exclude_folders:
                        folder_download_urls.extend(self.get_repo_download_urls_from_folder(folder_content['url']))
                else:
                    folder_download_urls.extend(self.get_repo_download_urls_from_folder(folder_content['url']))
        return folder_download_urls

    def get_repo_download_urls_json(self):
        repo_download_urls_json = json.dumps(self.repo_download_urls)
        return repo_download_urls_json

    def write_repo_download_urls_json(self):
        with open(f'{self.repo_name}_download_urls.json', 'w') as f:
            f.write(self.repo_download_urls_json)

if __name__ == '__main__':
    GitHubRepoDownloader("https://github.com/imageplaceholder/quotes/", [], [])
   # parser = argparse.ArgumentParser()
   # parser.add_argument('repo_url', help='GitHub repo url')
   # parser.add_argument('--exclude_file_names', nargs='+', help='List of file names to exclude')
   # parser.add_argument('--exclude_folders', nargs='+', help='List of folders to exclude')
   # args = parser.parse_args()
    #GitHubRepoDownloader(args.repo_url, args.exclude_file_names, args.exclude_folders)
