# A class that contains a block and a timer, used by the scheduler.

from object import Object

class ScheduleBlock(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
		# OBJECTS
		self.block = None # The block to use
		self.timer = None # The timer to use
