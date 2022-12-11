"""
1. Create a function to look for all json files in a GitHub user repos. And add JSON data & repo name to one single JSON file.
"""

import os
import json
import requests

def get_json_files(user):
    """
    Get all json files from a GitHub user repos.
    """
    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url)
    repos = response.json()
    json_files = []
    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["url"]
        repo_response = requests.get("https://api.github.com/repos/{}/{}/contents/".format(user, repo_name))
        repo_files = json.loads(json.dumps(repo_response.json()))
   #     repo_files = json.dumps(valid_response)


        for repo_file in repo_files:
            print(repo_file)
            if repo_file["name"].endswith(".json"):
                json_files.append(repo_file["download_url"])
    return json_files, repo_name

def get_json_data(json_files, repo_name):
    """
    Get JSON data from a list of JSON files.
    """
    json_data = []
    for json_file in json_files:
        response = requests.get(json_file)
        json_data.append(json.loads(json.dumps(response.json())))
      ##  json_data[-1]['repo_name'] = repo_name                 
        
    return json_data

def create_json_file(json_data, user):
    """
    Create a JSON file with JSON data & repo name.
    """
    json_file = {}
    json_file["data"] = json_data
    with open("{}.json".format(user), "w") as f:
        json.dump(json_file, f, indent=4)

def main():
    user = "imageplaceholder"
    json_files, repo_name = get_json_files(user)
    json_data = get_json_data(json_files, repo_name)
    create_json_file(json_data, user)

if __name__ == "__main__":
    main()
