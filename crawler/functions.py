from datetime import datetime


# Convert a timestamp to a more readable format
def readable_timetamp(timestamp):
	
	seconds = timestamp % 60
	timestamp //= 60
	minutes = timestamp % 60
	timestamp //= 60
	hours = timestamp
	
	return "%d:%d:%d" % (hours, minutes, seconds)


# Get the time left until a given time in a readable format
def get_readable_time_difference(timestamp):
	time_difference = abs(timestamp - int(datetime.now().timestamp()))
	return readable_timetamp(time_difference)
