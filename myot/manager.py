# This class manages how and when to play shows.

from object import Object

class Manager(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
	# NEXT -------------------------------------------------------------
	# Picks the next show (will still obey schedule times, even if
	# something is skipped)
	def next(self):
		pass
		
	# BACK -------------------------------------------------------------
	# Picks the previous show played.
	def back(self):
		pass
