# This class manages how and when to play shows.

from object import Object
from schedule import Schedule
from series import Series
from helpers import listDirs, listFiles
import settings


class Manager(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
		# OBJECTS
		self.scheduler = Schedule() # The schedule object
		self.series = [] # List of series
		self.autoblocks = [] # List of AutoBlocks
	
	# AUTO -------------------------------------------------------------
	# Automatically add series in a folder
	def auto(self, dir):
		#List all dirs
		dirs = listDirs(dir)
		
		for d in dirs[:]:
			series = Series()
			series.auto(d)
			
			# Check if auto found any files
			if len(series.video) != 0:
				self.series.append(series)
			
			else:
				dirs.remove(d)
			
	
	# NEXT -------------------------------------------------------------
	# Picks the next show (will still obey schedule times, even if
	# something is skipped)
	def next(self):
		pass
		
	# BACK -------------------------------------------------------------
	# Picks the previous show played.
	def back(self):
		pass
