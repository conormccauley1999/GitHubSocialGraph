from constants import *
from globals import *

from api import *
from database import *
from log import *

from github import Github
import mysql.connector


def crawl():
	global initial_rate_info

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

	db.close()


if __name__ == '__main__':
	crawl()
