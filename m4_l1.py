import subprocess
# FUNCTION TO RUN COMMANDS IN CMD


def run(command, local_path):
    try:
        result = subprocess.run(command, local_path, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Command failed with error:")
        print(e.stderr)
# SET GITHUB REPOSITORY URLS AS STR OBJECT


github_repo_urls = ["https://github.com/Stillyoung05/qwerty.git"]
# LOCAL PROJECTS PATH


paths = []
# RUN GIT


for m, f in github_repo_urls, paths:
    run("git init", f)
    run("git add .", f)
    run("git commit -m 'Initial commit'", f)
    run("git branch -M main", f)
    run(f"git remote add origin {m}", f)
    run("git push -u origin main", f)







