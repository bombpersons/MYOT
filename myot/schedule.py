import threading, time
import settings

from object import Object
from timer import Timer

# This class manages the tv's schedule (if used)
class Schedule(Object, threading.Thread):
	# INIT -------------------------------------------------------------
	# Init default vars
	def __init__(self):
		threading.Thread.__init__(self)
		Object.__init__(self)
		
		# VARS
		self.running = False # Whether or not the schedular is running
		self.blocks = [] # blocks active
		
	# ADD --------------------------------------------------------------
	# Add a scheduled time
	# 
	# block should be a Block instance, describing what to do at this time.
	def add(self, startTime, endTime, format, block):
		# Add this block
		newBlock = block
		
		# Start a timer for this block
		newBlock.timer = Timer()
		newBlock.timer.activate(startTime, endTime, format)
		
		# Add this block to the list
		self.blocks.append(newBlock)
		
		return
		
	# UDPDATE ----------------------------------------------------------
	# Call this every loop (or in a seperate process)
	def update(self):
		# Check what blocks are still active
		for block in self.blocks:
			print block.timer.set
			
			if not block.timer.set:
				# We can delete this one.
				self.blocks.remove(block)
		
		# Check which block we are using at the moment.
		for block in self.blocks:
			print block.timer.rung
			
			if block.timer.rung:
				# Call the block onChoose method before doing our's
				block.onChoose(self)
				
				# Send this to the picker
				picker = settings.PICKERS[block.picker]()
				episode = picker.pick(block)
				
				# Now play this
				print ("PLAYING " + episode.path)
				
				picker.save(block)
		

	# THREADING --------------------------------------------------------
	# START - Overriden start() method
	def start(self):
		self.running = True
		
		# Run the Threads method
		threading.Thread.start(self)
	
	# RUN - This is ran when the classes start() method is called.
	def run(self):
		while self.running:
			self.update()
			
			# Save some CPU
			time.sleep(settings.SCHEDULE_SLEEP)

