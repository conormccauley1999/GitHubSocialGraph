# Imports
from imports import *
from github import Github
import mysql.connector


# Explore an individual user
def exploreUser(db, gh, user):
	user_data = gh.get_user(user)
	print(user_data)
	return
