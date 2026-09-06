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

def get_all_branches():
    branches=run_git_command("git branch")
    return branches

def get_branch_count():
    no_of_branches=len(get_all_branches().splitlines())
    return no_of_branches


def get_recent_commits():
    commits=run_git_command("git log --oneline")
    return commits


def score():
    branch = get_current_branch()
    commits = get_commit_count()
    count_branches= get_branch_count()
    status = get_working_tree_status()
    recent_commits = get_recent_commits()
    total_score=0
    if status=="Clean":
        total_score+=30
    if commits>=5:
        total_score+=30
    elif commits == 3 or commits == 4:
        total_score += 20
    elif commits== 2 or commits== 1:
        total_score += 10
    if count_branches>=3:
        total_score+=20
    elif count_branches==2:
        total_score+=10
    elif count_branches==1:
        total_score+=5
    if recent_commits!="":
        total_score+=10
    if branch!="":
        total_score+=10
    return total_score

def score_status(health_score):
    if health_score>=90:
        return "Excellent"
    elif health_score>=75:
        return "Good"
    elif health_score>=50:
        return "Better"
    else:
        return "Try to improve"

def get_recommendations():
    if get_working_tree_status()=="Dirty":
        yield "Commit your pending changes"
        if get_commit_count()<=4:
            yield "Make more meaningful commits"
    if get_branch_count()==1:
        yield "Create/Use feature branches"







