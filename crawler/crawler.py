from constants import *
from database import *
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

	users_to_crawl = getUsersToCrawl(db)
	print users_to_crawl


if __name__ == '__main__':
	crawl()
