class RepositoryInformation:

	def __init__(self, repo_id, repo_obj):
		self.repo_id = repo_id
		self.full_name = repo_obj.full_name
		self.url = repo_obj.url
		self.is_fork = repo_obj.fork
		self.description = repo_obj.description
		self.fork_count = repo_obj.forks_count
		self.star_count = repo_obj.stargazers_count
		self.watcher_count = repo_obj.watchers_count
		self.size = repo_obj.size

	
	def get_insert_tuple(self):
		return (
			self.repo_id, self.full_name, self.url, self.is_fork, self.description,
			self.fork_count, self.star_count, self.watcher_count, self.size
		)
