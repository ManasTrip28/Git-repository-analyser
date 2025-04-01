from github import Github

def fetch_repo(username, repo_name, token):
    g = Github(token)
    repo = g.get_repo(f"{username}/{repo_name}")
    contents = repo.get_contents("")
    repo_data = {}
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            try:
                repo_data[file_content.path] = file_content.decoded_content.decode("utf-8")
            except:
                repo_data[file_content.path] = "Binary or non-UTF-8 content"
    return repo_data

def get_dir_structure(repo_data):
    print("Determining directory structure")
    structure = {}
    for filepath in repo_data.keys():
        parts = filepath.split("/")
        current = structure
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = None
    return structure


