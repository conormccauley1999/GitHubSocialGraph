from database import *
from functions import *
from globals import *
from RateInfo import *
from UserInformation import *
from github import Github
import mysql.connector


# Get the API query limit and number of queries remaining
def get_rate_info(gh):
	rate_obj = gh.get_rate_limit()
	time_left = get_readable_time_difference(gh.rate_limiting_resettime)	
	return RateInfo(rate_obj, gh.rate_limiting_resettime)


# Initialise query variables
def init_query_limit(gh):
	global initial_rate_info
	initial_rate_info = get_rate_info(gh)
	return initial_rate_info


# Explore an individual user
def explore_user(db, gh, user):
	user_obj = gh.get_user(user.user_name)
	user_info = UserInformation(user.user_id, user_obj)
	insert_user_information(db, user_info)
