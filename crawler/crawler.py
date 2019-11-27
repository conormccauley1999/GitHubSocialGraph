from constants import *
from api import *
from database import *
from functions import *
from log import *

from datetime import datetime
from github import Github
import mysql.connector


def crawl():

	log("CRAWLER STARTING", LogStatus.PASS)
	start_time = datetime.now()
	
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
		result = explore_user(db, gh, user)
		if result:
			log("Explored user: %s" % (user.user_name), LogStatus.PASS)
		else:
			log("Ignored user: %s" % (user.user_name), LogStatus.FAIL)

	repos = get_repos_to_explore(db)
	log("Found %d repo(s) to explore" % (len(repos)), LogStatus.INFO)

	for repo in repos:
		log("Exploring repo: %s" % (repo.repo_name), LogStatus.INFO)
		explore_repo(db, gh, repo)
		log("Explored repo: %s" % (repo.repo_name), LogStatus.PASS)

	end_rate_info = get_rate_info(gh)
	queries_made = initial_rate_info.remaining - end_rate_info.remaining

	end_time = datetime.now()
	update_crawler(db, start_time, end_time, queries_made)
	
	log("CRAWLER EXITING (made %d queries in %s)" % (queries_made, get_readable_time_difference(start_time.timestamp())), LogStatus.PASS)

	db.close()


if __name__ == '__main__':
	crawl()
