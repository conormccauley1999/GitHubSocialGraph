from constants import *
from Repository import *
from User import *

import mysql.connector


# Return a list of users that still need to be explored
def get_users_to_explore(db):
	cursor = db.cursor()
	cursor.execute(DBQ_USERS_TO_EXPLORE)
	users = [User(row[0], row[1], row[2]) for row in cursor.fetchall()]
	cursor.close()
	return users


# Return a list of repos that still need to be explored
def get_repos_to_explore(db):
	cursor = db.cursor()
	cursor.execute(DBQ_REPOS_TO_EXPLORE)
	repos = [Repository(row[0], row[1], row[2]) for row in cursor.fetchall()]
	cursor.close()
	return repos


# Return a dictionary of existing usernames and user IDs
def get_existing_users(db):
	
	existing_users = {}

	cursor = db.cursor()
	cursor.execute(DBQ_GET_EXISTING_USERS)

	for row in cursor.fetchall():
		existing_users[row[1]] = row[0]

	cursor.close()

	return existing_users


# Return set of existing follow pairs
def get_existing_follow_pairs(db):

	existing_follow_pairs = set()

	cursor = db.cursor()
	cursor.execute(DBQ_GET_EXISTING_FPAIRS)

	for row in cursor.fetchall():
		existing_follow_pairs.add((row[0], row[1]))

	cursor.close()

	return existing_follow_pairs


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


# Insert a new repo's information
def insert_repo_information(db, repo_info):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_INSERT_REPO_INFO, repo_info.get_insert_tuple())
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
def insert_children(db, parent_user_id, parent_depth, children_user_ids):
	data = []
	for child_user_id in children_user_ids:
		data.append((child_user_id, parent_user_id, parent_depth + 1))
	cursor = db.cursor(prepared = True)
	cursor.executemany(DBQ_INSERT_CHILDREN, data)
	db.commit()
	cursor.close()


# Mark a user as explored
def mark_user_as_explored(db, user_id):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_MARK_USER_EXPLORED, tuple([user_id]))
	db.commit()
	cursor.close()


# Mark a repo as explored
def mark_repo_as_explored(db, repo_id):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_MARK_REPO_EXPLORED, tuple([repo_id]))
	db.commit()
	cursor.close()


# Mark a user as ignored
def ignore_user(db, user_id):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_IGNORE_USER, tuple([user_id]))
	db.commit()
	cursor.close()


# Add a row to the Crawler table
def update_crawler(db, start_time, end_time, queries_made):
	cursor = db.cursor(prepared = True)
	cursor.execute(DBQ_UPDATE_CRAWLER, (start_time, end_time, queries_made))
	db.commit()
	cursor.close()
