import gitguard.analyzer as git


print("GitGuard Repository Health Analyzer")
print("-----------------------------------")


repository = git.get_repository_name()
branch = git.get_current_branch()
commits = git.get_commit_count()
status = git.get_working_tree_status()
branches = git.get_all_branches()
recent_commits = git.get_recent_commits()
branch_count=git.get_branch_count()
health_score=git.score()
score_level=git.score_status(health_score)
recommendation=git.get_recommendations()
owner,repo=git.get_remote_url()
info=git.get_github_info(owner,repo)




print("Repository Name:",repository)
print()

print("Current Branch:", branch)
print()

print("Total Commits:", commits)
print()

print("Working Tree Status:", status)
print()

print("Total no. of Branches:",branch_count)
print()

print(f'''Branches:
{branches}''')
print()

print(f"""Recent Commits:
{recent_commits}""")
print()

print("Score:",health_score)
print()
print("Score Status:",score_level)
print()

print("Recommendations:")
for recommend in recommendation:
    print(recommend)
print()


print("""GITHUB REPOSITORY
-------------------""")
print("Owner:",owner)
print("Repository Name:",repo)
print()

if info is not None:
    print("Stars:",info['stars'])
    print("Forks:",info['forks'])
    print("Open Issues:",info['issues'])
    print("Visibility:",info['visibility'])



