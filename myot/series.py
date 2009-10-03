# This class contains many video instances to represent a series.

class Series(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		# Call inherited __init__'s
		Object.__init__(self)
		
		# Vars
		self.videos = [] # A list of all the videos in this series.
		
	# AUTO -------------------------------------------------------------
	# Automatically scan a directory and populate videos.
	def auto(self, dir):
		pass
