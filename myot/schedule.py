from object import Object
from timer import Timer

# This class manages the tv's schedule (if used)
class Schedule(Object):
	# INIT -------------------------------------------------------------
	# Init default vars
	def __init__(self):
		Object.__init__(self)
		
	# ADD --------------------------------------------------------------
	# Add a scheduled time
	def add(self, startTime, endTime, format, program):
		pass
		
	# UDPDATE ----------------------------------------------------------
	# Call this every loop (or in a seperate process)
	def update(self):
		pass

