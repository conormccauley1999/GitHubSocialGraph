from imports import *
from datetime import datetime
from enum import Enum


# Basic enum for log statuses
class LogStatus(Enum):
	PASS = 1
	INFO = 2
	WARN = 3
	FAIL = 4


# Convert a LogStatus enum to a string
def getLogStatusText(status):
	if status == LogStatus.PASS:
		return "PASS"
	elif status == LogStatus.INFO:
		return "INFO"
	elif status == LogStatus.WARN:
		return "WARN"
	elif status == LogStatus.FAIL:
		return "FAIL"
	else:
		return "????"


# Log a message to the terminal and a text file
def log(message, status = LogStatus.INFO):

	# Format the output string
	output = "[%s], %s, %s" % (getLogStatusText(status), str(datetime.now()), message)

	# Log to the screen
	if LOG_TO_SCREEN:
		print(output)
	
	# Log to the output file
	if LOG_TO_FILE:
		open(LOG_FILE, "a").write(output + "\n")
