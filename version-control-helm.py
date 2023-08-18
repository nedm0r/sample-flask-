import sys
import requests
import yaml
from packaging.version import Version

requests.packages.urllib3.disable_warnings()
def compare_versions(v1, v2):
    return Version(v1) > Version(v2)

def get_highest_version(repository):
    url = f"https://hub.docker.com/v2/repositories/nedm0r/{repository}/tags/?page_size=100"
    response = requests.get(url, verify=True)  # Set verify=True to enable SSL verification
    if response.status_code == 200:
        data = response.json()
        tags = data["results"]
        if not tags:
            return None
        max_version = None
        for tag in tags:
            tag_name = tag["name"]
            if tag_name == "latest":
                continue
            if max_version is None or compare_versions(tag_name, max_version):
                max_version = tag_name
        return max_version

def update_values_yaml(repository, new_version):
    with open("values.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)


    if repository == "docker-flask-project":
        yaml_data["myFlaskApp"]["image"]["tag"] = new_version
    elif repository == "flask-database":
        yaml_data["mysql"]["image"]["tag"] = new_version
    else:
        print(f"Error: Unsupported repository '{repository}'")
        return

    with open("values.yaml", "w") as file:
        yaml.dump(yaml_data, file, default_flow_style=False)

if __name__ == "__main__":
    repository_names = ["docker-flask-project", "flask-database"]
    for repo in repository_names:
        highest_version = get_highest_version(repo)
        if highest_version:
            print(f"The highest version for {repo} is: {highest_version}")
            update_values_yaml(repo, highest_version)
            print("values.yaml updated successfully.")
        else:
            print(f"No versions found for {repo}")
