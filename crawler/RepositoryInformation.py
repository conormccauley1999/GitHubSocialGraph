class RepositoryInformation:

	def __init__(self, repo_id, repo_obj):
		self.repo_id = repo_id
		self.full_name = ""
		self.url = ""
		self.is_fork = False
		self.description = ""
		self.fork_count = 0
		self.star_count = 0
		self.watcher_count = 0
		self.repo_obj = repo_obj # to-do: remove

	
	def get_insert_tuple(self):
		return (
			self.repo_id, self.full_name, self.url, self.is_fork, self.description,
			self.fork_count, self.star_count, self.watcher_count
		)
