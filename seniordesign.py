from github import Github

# Authenticate with GitHub
g = Github('<PAT>') # Replace <PAT> with your personal access token

# Get the repository
repo = g.get_repo('owner/repo') # Replace 'owner/repo' with the name of your repository

# Determine which actions have permissions set on the repo
actions = repo.get_actions()
if not actions.permissions:
    print('No actions have permissions set on the repo')
else:
    for action in actions.permissions:
        print(f'{action} has permissions set on the repo')

# Determine if pipelines are configured for commits
pipelines = repo.get_workflows()
if not pipelines.totalCount:
    print('No pipelines are configured for commits')
else:
    print(f'{pipelines.totalCount} pipelines are configured for commits')

# Determine if new branches are configured for actions on commits
branch_protection = repo.get_branch_protection('main') # Replace 'main' with the name of your default branch
if not branch_protection.restrictions:
    print('New branches are not configured for actions on commits')
else:
    print('New branches are configured for actions on commits')