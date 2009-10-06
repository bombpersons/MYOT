# This is a class that schedules tasks. It will call it's ring() funtion
# when the timer starts, and call it's running() function when within the
# time limit, and call it's over() function when the time is up.

# This class uses SYSTEM time.

import time, threading
import settings

from object import Object

class Timer(Object, threading.Thread):
	# INIT -------------------------------------------------------------
	# Init vars
	#
	# If autotick is True (default) the timer will run in a seperate
	# process. Other wise it will need to be updated automatically by
	# calling tick()
	def __init__(self, autotick=True):
		# Call inherited __init__ first.
		threading.Thread.__init__(self)
		Object.__init__(self)
		
		# Now our vars
		self.startTimeString = "" # The time when the timer starts as a string
		self.endTimeString = "" # The time when the timer stops as a string
		self.timeFormat = "" # The string to use as the format for the string		
		self.set = False # The timer starts deactivated
		self.process = autotick # Wether or not to run in a seperate process.
		self.rung = False # Has the timer rang yet?
		
		
	# ACTIVATE --------------------------------------------------------------
	# Sets the timer
	def activate(self, startTime, endTime, format):
		# Set the timer.
		self.startTimeString = startTime
		self.endTimeString = endTime
		self.timeFormat = format
		
		# Conver the strings to time using format
		try:
			self.startTime = time.strptime(startTime, self.timeFormat)
			self.endTime = time.strptime(endTime, self.timeFormat)
		except ValueError:
			# Error
			print ("Error: Cannot convert time according to format")
			return False
		
		# Try and convert the time to seconds
		try:
			self.startTimeSecs = time.mktime(self.startTime)
			self.endTimeSecs = time.mktime(self.endTime)
		except OverflowError, ValueError:
			# Error
			print ("Error: Cannot convert time to seconds")
			return False
		
		# The timer is now set
		self.set = True
		
		# If self.process is true, we need to start calling tick in a
		# seperate process.
		if self.process:
			self.deamon = True # We don't want python to hang if a timer
							    # is still running at exit.
			self.start()
	
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
		# Check the time
		if time.mktime(time.localtime()) > self.startTimeSecs and time.mktime(time.localtime()) < self.endTimeSecs and not self.rung:
			# The time has come =)
			# Call ring()
			self.ring()
			
			# Now set self.rung to True
			self.rung = True
		
		# If the time is up..
		elif time.mktime(time.localtime()) > self.endTimeSecs and self.rung:
			self.over()
			
			# Unset the timer
			self.set = False
			self.rung = False
		
		# If we are inbetween the starttime and endtime.
		elif time.mktime(time.localtime()) > self.startTimeSecs and time.mktime(time.localtime()) < self.endTimeSecs and self.rung:
			self.running()
			
		# If any of those aren't true, then the timer hasn't started yet
		else:
			# Check if the endTime has already passed
			if time.mktime(time.localtime()) > self.endTimeSecs:
				
				# The time has already passed.
				self.set = False
				
		
	# THREADING STUFF --------------------------------------------------
	# This is run by Threads start() method.
	def run(self):
		while self.set == True:
			# Tick
			self.tick()
			
			# Sleep for a bit to save CPU
			time.sleep(settings.TIMER_SLEEP)
