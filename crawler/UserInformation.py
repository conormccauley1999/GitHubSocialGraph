from functions import *


class UserInformation:

	def __init__(self, user_id, user_obj):
		self.user_id = user_id
		self.name = user_obj.name
		self.avatar_url = user_obj.avatar_url
		self.company = user_obj.company
		self.location = user_obj.location
		self.email = user_obj.email
		self.bio = user_obj.bio
		self.repository_count = user_obj.public_repos
		self.follower_count = user_obj.followers
		self.following_count = user_obj.following
		self.user_obj = user_obj # to-do: remove