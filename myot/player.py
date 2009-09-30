# This base class controls how to play files. It basically just calls
# a media player in a seperate process and returns information about the
# process (time played, whether or not it is still playing, etc)

class Player:
	# INIT -------------------------------------------------------------
	# This function is called when the class is instantated
	# Default vars are defined etc,
	def __init__(self):
		pass
		
	# GETINFO ----------------------------------------------------------
	# Get's info about this process (This is intended to be overridden)
	def get(self, key):
		pass

	# PLAY -------------------------------------------------------------
	# (This is intended to be overridden)
	def play(self):
		pass
		
	# STOP -------------------------------------------------------------
	# (This is intended to be overridden)
	def stop(self):
		pass
		
	# PAUSE ------------------------------------------------------------
	def pause(self):
		pass
		
	
