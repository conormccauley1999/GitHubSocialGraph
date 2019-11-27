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
MAX_USERS		= 10
MAX_REPOS		= 50
MAX_USER_REPOS	= 50
MAX_FOLLOWERS	= 50
MAX_FOLLOWEES 	= 50


# Database Queries
DBQ_USERS_TO_EXPLORE 	= "select UserId, Username, UserDepth from UsersToExplore limit %d" % (MAX_USERS)
DBQ_REPOS_TO_EXPLORE	= "select RepositoryId, Username, RepositoryName from RepositoriesToExplore limit %d" % (MAX_REPOS)

DBQ_INSERT_USER_INFO	= "insert into UserInformation (UserId, Name, Url, AvatarUrl, Company, Location, Email, Bio, RepositoryCount, FollowerCount, FollowingCount) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
DBQ_INSERT_REPO_INFO	= "insert into RepositoryInformation (RepositoryId, FullName, Url, IsFork, Description, ForkCount, StarCount, WatcherCount, Size) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

DBQ_INSERT_BLANK_USER	= "insert into User (IsExplored, Username, LastCrawled) values (false, %s, null)"
DBQ_INSERT_BLANK_REPO	= "insert into Repository (UserId, IsExplored, Name, LastCrawled) values (%s, false, %s, null)"

DBQ_MARK_USER_EXPLORED	= "update User set IsExplored = true, LastCrawled = now() where Id = %s"
DBQ_MARK_REPO_EXPLORED	= "update Repository set IsExplored = true, LastCrawled = now() where Id = %s"

DBQ_INSERT_FOLLOW		= "insert into Follow (FollowerUserId, FollowingUserId) values (%s, %s)"
DBQ_INSERT_CHILDREN		= "insert into UserRelationship (UserId, ParentUserId, CurrentDepth) values (%s, %s, %s)"

DBQ_IGNORE_USER			= "update User set `Ignore` = true where Id = %s"
DBQ_GET_USER_ID			= "select GetUserId('%s')"
DBQ_GET_EXISTING_USERS 	= "select Id, Username from User"
DBQ_GET_EXISTING_FPAIRS	= "select FollowerUserId, FollowingUserId from Follow"
DBQ_UPDATE_CRAWLER		= "insert into Crawler (StartTime, EndTime, QueriesMade) values (%s, %s, %s)"
