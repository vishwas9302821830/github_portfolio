import gitguard.analyzer as git

print("GitGuard Repository Report")
print("----------------------------")
repository = git.get_repository_name()
branch = git.get_current_branch()
commits = git.get_commit_count()
status = git.get_working_tree_status()

print("Repository Name:",repository)
print("Current Branch:", branch)
print("Total Commits:", commits)
print("Working Tree Status:",status)
