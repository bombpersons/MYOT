# Each instance of this class is an seperated program / series.
# Most managers will automatically create these from folders.

from object import ItemObject

class Program(ItemObject):
	# INIT -------------------------------------------------------------
	def __init__(self):
		ItemObject.__init__(self)
		
	# AUTO -------------------------------------------------------------
	# This will automatically scan a directory for files and use the
	# the directory's name.
	def auto(self, dir):
		pass
