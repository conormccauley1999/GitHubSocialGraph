import os # for accessing environment variables


# API and Database Connections
API_KEY 	= os.environ['GH_API_TOKEN']
DB_SERVER 	= os.environ['GH_DB_SERVER']
DB_USER 	= os.environ['GH_DB_USER']
DB_PASS 	= os.environ['GH_DB_PASS']
DB_NAME 	= os.environ['GH_DB_NAME']
DB_PORT 	= 3306


# Logging
LOG_TO_SCREEN 	= True
LOG_TO_FILE 	= False
LOG_FILE		= "..\\logs\\crawler_log.txt"


# Miscellaneous
NONE = -1


# Database Queries
DBQ_USERS_TO_EXPLORE 	= "select UserId, Username from UsersToExplore"
DBQ_INSERT_USER_INFO	= "insert into UserInformation (UserId, Name, Url, AvatarUrl, Company, Location, Email, Bio, RepositoryCount, FollowerCount, FollowingCount) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
