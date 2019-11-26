from constants import *
from api import *
from database import *
from log import *

from github import Github
import mysql.connector


def crawl():
	
	gh = Github(API_KEY)
	db = mysql.connector.connect(
		host = DB_SERVER,
		user = DB_USER,
		passwd = DB_PASS,
		database = DB_NAME
	)

	initial_rate_info = get_rate_info(gh)
	log("%d/%d API queries remaining (resets in %s)" % (initial_rate_info.remaining, initial_rate_info.limit, initial_rate_info.reset), LogStatus.INFO)

	users = get_users_to_explore(db)
	log("Found %d user(s) to explore" % (len(users)), LogStatus.INFO)

	for user in users:
		log("Exploring user: %s" % (user.user_name), LogStatus.INFO)
		explore_user(db, gh, user)
		log("Explored user: %s" % (user.user_name), LogStatus.PASS)

	#repos = get_repos_to_explore(db)
	#log("Found %d repo(s) to explore" % (len(repos)), LogStatus.INFO)

	#for repo in repos:
		#log("Exploring repo: %s" % (repo.repo_name), LogStatus.INFO)
		#explore_repo(db, gh, repo)
		#log("Explored repo: %s" % (repo.repo_name), LogStatus.PASS)

	end_rate_info = get_rate_info(gh)

	db.close()


if __name__ == '__main__':
	crawl()
