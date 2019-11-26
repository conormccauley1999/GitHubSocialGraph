from constants import *
from datetime import datetime
from enum import Enum


class LogStatus(Enum):
	PASS = 1
	INFO = 2
	WARN = 3
	FAIL = 4


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


def log(message, status = LogStatus.INFO):
	output = "[%s], %s, %s\n" % (statusString, str(datetime.now()), message)
	with open(LOG_FILE, 'a') as f:
		f.write(output)
