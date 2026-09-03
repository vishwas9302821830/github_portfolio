import subprocess as sp


def run_git_command(cmd):
    command = cmd.split()
    result = sp.run(command, check=True, capture_output=True, text=True)
    result = result.stdout.strip()
    return result


def get_current_branch():
    current_branch = run_git_command("git branch --show-current")
    return  current_branch


def get_commit_count():
    result = run_git_command("git log --oneline")
    no_of_commits = len(result.splitlines())
    return no_of_commits


def get_working_tree_status():

    result = run_git_command("git status --porcelain")
    if result == "":
        return  "Clean"
    else:
        return "Dirty"


def get_repository_name():

    path = run_git_command("git rev-parse --show-toplevel")
    repo = path.split("/")[-1]

    return  repo
