from datetime import datetime, timedelta


# Get the time left until a given time in a readable format
def get_readable_time_difference(timestamp):
	time_difference = abs(timestamp - int(datetime.now().timestamp()))
	return timedelta(seconds = time_difference)
