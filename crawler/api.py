from database import *
from functions import *
from log import *
from RateInfo import *
from UserInformation import *

from github import Github
import mysql.connector


# Get the API query limit and number of queries remaining
def get_rate_info(gh):
	rate_obj = gh.get_rate_limit()
	time_left = get_readable_time_difference(gh.rate_limiting_resettime)	
	return RateInfo(rate_obj, gh.rate_limiting_resettime)


# Explore an individual user
def explore_user(db, gh, user):

	# Insert some information about the user
	log("Inserting information for user: %s" % (user.user_name), LogStatus.INFO)
	user_obj = gh.get_user(user.user_name)
	user_info = UserInformation(user.user_id, user_obj)
	insert_user_information(db, user_info)

	# Insert the user's own repositories
	user_repos = user_obj.get_repos()
	log("Found %d repo(s) for user: %s" % (user_repos.totalCount, user.user_name), LogStatus.INFO)
	log("Inserting repo data for %d repos for user: %s" % (user_repos.totalCount, user.user_name), LogStatus.INFO)
	for repo in user_repos:
		insert_blank_repository(db, user.user_id, repo.name)

	# Insert the user's followers and people the user is following
	follow_id_pairs = set()
	new_user_ids = set()
	existing_users = get_existing_users(db)

	followers = user_obj.get_followers()
	log("Found %d follower(s) for user: %s" % (followers.totalCount, user.user_name), LogStatus.INFO)

	for follower in followers:
		if follower.login not in existing_users:
			insert_blank_user(db, follower.login)
			follower_user_id = get_user_id(db, follower.login)
			existing_users[follower.login] = follower_user_id
			new_user_ids.add(follower_user_id)
		follow_id_pairs.add((existing_users[follower.login], user.user_id))

	following = user_obj.get_following()
	log("Found %d following for user: %s" % (following.totalCount, user.user_name), LogStatus.INFO)

	for followee in following:
		if followee.login not in existing_users:
			insert_blank_user(db, followee.login)
			followee_user_id = get_user_id(db, followee.login)
			existing_users[followee.login] = followee_user_id
			new_user_ids.add(followee_user_id)
		follow_id_pairs.add((user.user_id, existing_users[followee.login]))

	log("Inserting follow data for %d user pairs for user: %s" % (len(follow_id_pairs), user.user_name), LogStatus.INFO)
	insert_follow(db, follow_id_pairs)

	# Mark new users as children of the current user
	log("Marking %d new users as children of user: %s" % (len(new_user_ids), user.user_name), LogStatus.INFO)
	mark_as_children(db, user.user_id, user.user_depth, new_user_ids)

	# Mark the user as explored
	log("Marking '%s' as explored" % (user.user_name), LogStatus.INFO)
	mark_as_explored(db, user.user_id)
