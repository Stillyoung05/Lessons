import subprocess

def push_to_github(repo_url, local_path):
    try:
        # Clone the repository
        subprocess.run(['git', 'clone', repo_url, local_path], check=True)

        # Perform changes in the local repository (e.g., add, commit, etc.)

        # Push changes to GitHub
        subprocess.run(['git', 'push', 'origin', 'master'], check=True, cwd=local_path)

        print(f"Pushed changes to {repo_url}")

    except subprocess.CalledProcessError as e:
        print(f"Failed to push changes to {repo_url} with error:")
        print(e.stderr)

# Example usage:
repo_urls = [
    "https://github.com/username/repo1.git",
    "https://github.com/username/repo2.git",
    # Add more repository URLs as needed
]

for url in repo_urls:
    # Extract repository name from the URL and use it as the local path
    repo_name = url.split('/')[-1].replace('.git', '')
    local_path = f"./{repo_name}"

    push_to_github(url, local_path)
