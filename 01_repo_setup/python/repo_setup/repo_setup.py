from github import Github
from github import Auth

import argparse
import json

def githubRepositoryList(github_token):

    auth = Auth.Token(github_token)
    g = Github(auth=auth)

    for repo in g.get_user().get_repos():
        print(repo.name)

    # To close connections after use
    g.close()

def main(repository_list_json, github_token):
    print("Python script is starting...")
    print(f"Opening {repository_list_json}:")


    with open(repository_list_json, "r") as f:
        repository_list_json = json.load(f)

    repository_list = repository_list_json["repositories"]

    print("Repository list:")
    for repo in repository_list:
        print(repo)

    print("Currently available GitHub repsoitories:")
    githubRepositoryList(github_token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get a JSON file with repository list"
    )
    parser.add_argument("--json_repository_list_path", required=True, type=str)
    parser.add_argument("--github_token", required=True, type=str)
    args = parser.parse_args()

    main(args.json_repository_list_path, args.github_token)