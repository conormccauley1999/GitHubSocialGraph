from constants import *
from User import *
import mysql.connector


# Return a list of users that still need to be explored
def get_users_to_explore(db):
	cursor = db.cursor()
	cursor.execute(DBQ_USERS_TO_EXPLORE)
	users = [User(row[0], row[1]) for row in cursor.fetchall()]
	return users


# Insert a new users information
def insert_user_information(db, user_info):
	print(user_info)
	return
