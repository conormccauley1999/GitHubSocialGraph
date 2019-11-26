from functions import *


class RateInfo:

	def __init__(self, rate_obj, reset_time):
		self.remaining = rate_obj.core.remaining
		self.limit = rate_obj.core.limit
		self.reset = get_readable_time_difference(reset_time)
