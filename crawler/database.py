# Imports
from imports import *
import mysql.connector


# Return a list of users that still need to be explored
def getUsersToExplore(db):
	cursor = db.cursor()
	cursor.execute(DBQ_USERS_TO_EXPLORE)
	result = [row[0] for row in cursor.fetchall()]
	return result
