from constants import *
import mysql.connector


# Return a list of users that still need to be explored
def get_users_to_explore(db):
	cursor = db.cursor()
	cursor.execute(DBQ_USERS_TO_EXPLORE)
	users = [row[0] for row in cursor.fetchall()]
	return users
