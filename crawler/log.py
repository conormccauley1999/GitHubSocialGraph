from constants import *
from datetime import datetime
from enum import Enum


# Basic enum for log statuses
class LogStatus(Enum):
	PASS = 1
	INFO = 2
	WARN = 3
	FAIL = 4


# Convert a LogStatus enum to a string
def get_log_status_text(status):
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

	output = "[%s], %s, %s" % (get_log_status_text(status), str(datetime.now()), message)

	if LOG_TO_SCREEN:
		print(output)
	if LOG_TO_FILE:
		with open(LOG_FILE, "a") as f:
			f.write(output + "\n")
