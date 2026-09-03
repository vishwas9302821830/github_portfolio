import gitguard.analyzer as git

print("GitGuard Repository Report")
print("----------------------------")


repository = git.get_repository_name()
branch = git.get_current_branch()
commits = git.get_commit_count()
status = git.get_working_tree_status()
branches=git.get_all_branches()
recent_commits=git.get_recent_commits()
print("Repository Name:",repository)
print()
print("Current Branch:", branch)
print()
print("Total Commits:", commits)
print()
print("Working Tree Status:",status)
print()
print(f'''Branches:
{branches}''')
print()
print(f"""Recent Commits:
{recent_commits}""")
