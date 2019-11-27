from constants import *
from User import *

import mysql.connector


# Return a list of users that still need to be explored
def get_users_to_explore(db, max = MAX_USERS):
	cursor = db.cursor()
	cursor.execute(DBQ_USERS_TO_EXPLORE)
	users = [User(row[0], row[1], row[2]) for row in cursor.fetchall()]
	cursor.close()
	if len(users) > MAX_USERS: users = users[:MAX_USERS]
	return users


# Return a dictionary of existing usernames and user IDs
def get_existing_users(db):
	
	existing_users = {}

	cursor = db.cursor()
	cursor.execute(DBQ_GET_EXISTING_USERS)

	for row in cursor.fetchall():
		existing_users[row[1]] = row[0]

	cursor.close()

	return existing_users


# Get the ID of a specific user
def get_user_id(db, user_name):
	cursor = db.cursor()
	query = DBQ_GET_USER_ID % (user_name)
	cursor.execute(query)
	user_id = cursor.fetchone()[0]
	cursor.close()
	return user_id


# Insert a new user's information
def insert_user_information(db, user_info):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_INSERT_USER_INFO, user_info.get_insert_tuple())
	db.commit()
	cursor.close()


# Insert an unexplored user
def insert_blank_user(db, user_name):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_INSERT_BLANK_USER, tuple([user_name]))
	db.commit()
	cursor.close()


# Insert an unexplored repository
def insert_blank_repository(db, user_id, repo_name):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_INSERT_BLANK_REPO, (user_id, repo_name))
	db.commit()
	cursor.close()


# Insert a row into the Follow table for each pair of IDs
def insert_follow(db, follow_id_pairs):
	cursor = db.cursor(prepared = True)
	cursor.executemany(DBQ_INSERT_FOLLOW, list(follow_id_pairs))
	db.commit()
	cursor.close()


# Insert rows for new child users
def mark_as_children(db, parent_user_id, parent_depth, children_user_ids):
	return


# Mark a user as explored
def mark_as_explored(db, user_id):
	return
