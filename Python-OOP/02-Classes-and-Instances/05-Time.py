# 05. Time 
from datetime import datetime, timedelta


class Time:
	max_hours = 23					# only for judge
	max_minutes = 59				# only for judge
	max_seconds = 59				# only for judge

	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		self.time_obj = datetime(100, 1, 1, hours, minutes, seconds)
	
	def set_time(self, hours, minutes, seconds):
		self.time_obj = datetime(100, 1, 1, hours, minutes, seconds)
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
		
	def get_time(self):
		return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
		
	def next_second(self):
		self.time_obj += timedelta(seconds=1)
		self.hours = self.time_obj.hour
		self.minutes = self.time_obj.minute
		self.seconds = self.time_obj.second
		return self.get_time()


# Test Code:
"""
time = Time(9, 30, 59)
print(time.next_second())
time2 = Time(10, 59, 59)
print(time2.next_second())
time3 = Time(23, 59, 59)
print(time3.next_second())
"""















