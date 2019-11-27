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
MAX_USERS	= 100


# Database Queries
DBQ_USERS_TO_EXPLORE 	= "select UserId, Username, UserDepth from UsersToExplore"
DBQ_REPOS_TO_EXPLORE	= ""

DBQ_GET_USER_ID			= "select GetUserId('%s')"
DBQ_GET_EXISTING_USERS 	= "select Id, Username from User"

DBQ_INSERT_USER_INFO	= "insert into UserInformation (UserId, Name, Url, AvatarUrl, Company, Location, Email, Bio, RepositoryCount, FollowerCount, FollowingCount) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
DBQ_INSERT_REPO_INFO	= ""

DBQ_INSERT_BLANK_USER	= "insert into User (IsExplored, Username, LastCrawled) values (false, %s, null)"
DBQ_INSERT_BLANK_REPO	= "insert into Repository (UserId, IsExplored, Name, LastCrawled) values (%s, false, %s, null)"

DBQ_INSERT_FOLLOW		= "insert into Follow (FollowerUserId, FollowingUserId) values (%s, %s)"
