# Imports
from imports import *
from github import Github
import mysql.connector


# Entry method
def crawl():

	# Set up our connections
	gh = Github(API_KEY)
	db = mysql.connector.connect(
		host=DB_SERVER,
		user=DB_USER,
		passwd=DB_PASS,
		database=DB_NAME
	)

	# Get a list of users we still need to explore
	users = getUsersToExplore(db)
	log("Found %s users to explore" % (len(users)), LogStatus.INFO)

	# Explore each user
	for user in users:
		log("Exploring user: %s" % (user), LogStatus.INFO)
		exploreUser(db, gh, user)


# So we don't accidentally run the entry method multiple times
if __name__ == '__main__':
	crawl()
