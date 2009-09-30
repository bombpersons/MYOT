# This is a class that schedules tasks. It will call it's ring() funtion
# when the timer starts, and call it's running() function when within the
# time limit, and call it's over() function when the time is up.

# This class uses SYSTEM time.

class Timer:
	# INIT -------------------------------------------------------------
	# Init vars
	def __init__(self):
		pass
		
	# SET --------------------------------------------------------------
	# Sets the timer
	def set(self, startTime, endTime, format):
		pass
	
	# RING -------------------------------------------------------------
	# This function is called when the timer starts.
	def ring(self):
		pass

	# RUNNING ----------------------------------------------------------
	# Called when the the time is whithin the time limits.
	def running(self):
		pass
	
	# OVER -------------------------------------------------------------
	# Called when the time is up
	def over(self):
		pass
		
	# TICK -------------------------------------------------------------
	# Call this every loop (or in a seperate process)
	def tick(self):
		pass
