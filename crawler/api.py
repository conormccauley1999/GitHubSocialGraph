from functions import *
from globals import *
from github import Github
import mysql.connector


# Get the API query limit and number of queries remaining
def get_rate_info(gh):
	rate_obj = gh.get_rate_limit()
	time_left = get_readable_time_difference(gh.rate_limiting_resettime)	
	return (rate_obj.core.remaining, rate_obj.core.limit, time_left)


# Initialise query variables
def init_query_limit(gh):
	global query_limit, query_usage
	rate_info = get_rate_info(gh)
	query_usage = rate_info[0]
	query_limit = rate_info[1]
	return rate_info


# Explore an individual user
def explore_user(db, gh, user):
	user_obj = gh.get_user(user)
	return
