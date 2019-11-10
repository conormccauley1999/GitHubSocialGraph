from github import Github
import os

gh = Github(os.environ['GH_API_TOKEN'])

for repo in gh.get_user().get_repos():
	print(repo.name)
