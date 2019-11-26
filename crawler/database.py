from constants import *
from log import *
import mysql.connector


def getUsersToCrawl(db):
	cursor = db.cursor()
	cursor.execute("select Name from UsersToCrawl")
	result = [row[0] for row in cursor.fetchall()]
	return result
