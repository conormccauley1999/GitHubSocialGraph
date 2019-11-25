import os # for accessing environment variables

# API and Database Connections
API_KEY 	= os.environ['GH_API_TOKEN']
DB_SERVER 	= os.environ['GH_DB_SERVER']
DB_USER 	= os.environ['GH_DB_USER']
DB_PASS 	= os.environ['GH_DB_PASS']
DB_NAME 	= os.environ['GH_DB_NAME']
DB_PORT 	= 3306
