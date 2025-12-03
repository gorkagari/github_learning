import argparse
import json

def main(repository_list_json):
    print("Python script is starting...")
    print(f"Opening {repository_list_json}:")


    with open(repository_list_json, "r") as f:
        repository_list = json.load(f)
    print(repository_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get a JSON file with repository list"
    )
    parser.add_argument("--json_repository_list_path", required=True, type=str)
    args = parser.parse_args()

    main(args.json_repository_list_path)