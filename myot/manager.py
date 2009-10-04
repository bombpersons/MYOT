# This class manages how and when to play shows.

import threading, time

from object import Object
from schedule import Schedule
from series import Series

from helpers import listDirs, listFiles
from week import getDate

import settings, schedule_settings

class Manager(Object, threading.Thread):
	# INIT -------------------------------------------------------------
	def __init__(self):
		threading.Thread.__init__(self)
		Object.__init__(self)
		
		# OBJECTS
		self.scheduler = Schedule() # The schedule object
		self.series = [] # List of series
	
	# LOAD -------------------------------------------------------------
	# Loads schedule from a file (schedule_settings.py).
	def load(self):
		# Add blocks
		for block in schedule_settings.BLOCKS:
			# Calculate the day
			start_day = str(getDate(block[1].split()[0]))
			end_day = str(getDate(block[2].split()[0]))
			
			self.scheduler.add(start_day + " " + block[1].split()[1], end_day + " " + block[2].split()[1], "%j %H:%M", block[0])
		
		# Start the scheduler (if it isn't already)
		if not self.scheduler.running:
			self.scheduler.start()
			
			# Also start the manager
			self.start()
	
	# NEXT -------------------------------------------------------------
	# Picks the next show (will still obey schedule times, even if
	# something is skipped)
	def next(self):
		pass
		
	# BACK -------------------------------------------------------------
	# Picks the previous show played.
	def back(self):
		pass
		
	# THREADING --------------------------------------------------------
	def run(self):
		while self.scheduler.running:
			time.sleep(settings.MANAGER_SLEEP)
			self.load()
