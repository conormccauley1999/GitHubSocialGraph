from api import *
from constants import *
from database import *
from globals import *
from log import *
from github import Github
import mysql.connector


def crawl():

	gh = Github(API_KEY)
	db = mysql.connector.connect(
		host=DB_SERVER,
		user=DB_USER,
		passwd=DB_PASS,
		database=DB_NAME
	)

	rate_info = init_query_limit(gh)
	log("%d/%d API queries remaining (resets in %s)" % (rate_info[0], rate_info[1], rate_info[2]), LogStatus.INFO)

	users = get_users_to_explore(db)
	log("Found %s users to explore" % (len(users)), LogStatus.INFO)

	for user in users:
		log("Exploring user: %s" % (user), LogStatus.INFO)
		explore_user(db, gh, user)


if __name__ == '__main__':
	crawl()
