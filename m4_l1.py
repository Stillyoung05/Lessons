import subprocess
# FUNCTION TO RUN COMMANDS IN CMD


def run(command):
    try:
        result = subprocess.run(command, check=True)
        print("Command output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Command failed with error:")
        print(e.stderr)
# SET GITHUB REPOSITORY URLS AS STR OBJECT


github_repo_urls = ["https://github.com/Stillyoung05/qwerty.git"]
# RUN GIT


for m in github_repo_urls:
    run("git add .")
    run("git commit -m 'Initial commit'")
    run("git branch -M main")
    run(f"git remote add origin {m}")
    run("git push -u origin main")







