import threading, time
import settings

from object import Object
from timer import Timer
from schedule_block import ScheduleBlock

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
		self.player = settings.PLAYERS[settings.PLAYER]()
		self.play_advert = False
		
	# ADD --------------------------------------------------------------
	# Add a scheduled time
	# 
	# block should be a Block instance, describing what to do at this time.
	def add(self, startTime, endTime, format, block):
		# Make a new ScheduleBlock
		newBlock = ScheduleBlock()
		
		# Add this block
		newBlock.block = block
		
		# Make a timer
		newBlock.timer = Timer()
		
		# Figure out the time
		year = time.strftime("%Y")
		
		# Add the block timer
		newBlock.timer.activate(year + " " + startTime, year + " " + endTime, "%Y " + format)
		
		# Add this block to the list
		self.blocks.append(newBlock)
		
		return
		
	# UDPDATE ----------------------------------------------------------
	# Call this every loop (or in a seperate process)
	def update(self):
		# Check what blocks are still active
		for block in self.blocks[:]:
			if not block.timer.set:
				# We can delete this one.
				self.blocks.remove(block)
		
		# Check which block we are using at the moment.
		for block in self.blocks:
			block.timer.tick()
			#print block.name
			if block.timer.rung:
				# Check if this is a new block
				if block.block.current != True:
					# This isn't a new block, stop the player
					self.player.stop()
				
				# If we aren't playing and adverts are enabled, play them here.
				if not self.player.get('playing') and block.block.use_ads and self.play_advert:
					
					# Make a picker
					picker = settings.PICKERS[block.ad_picker]()
					advert = picker.pickAd(block.block)
					
					# Play it
					print ("PLAYING ADVERT " + advert.path)
					self.player.play(advert)
					
					# Finished playing adverts
					self.play_advert = False
				
				# Check if we aren't already playing
				if not self.player.get('playing'):
				
					# Call the block onChoose method before doing our's
					block.block.onChoose(self)
					
					# Send this to the picker
					picker = settings.PICKERS[block.block.picker]()
					episode = picker.pick(block.block)
					
					# Now play this
					print ("PLAYING " + episode.path)
					self.player.play(episode)
					
					# Save the block
					picker.save(block.block)
					
					# If we have adverts enabled,  set the play_advert to true
					if block.block.use_ads:
						self.play_advert = True
					
				#Set this block to current
				block.block.current = True
			 
			 # There is no block to play yet
			#else:
			#	print ("No Block to play... (Channel is of Air)")
		

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

