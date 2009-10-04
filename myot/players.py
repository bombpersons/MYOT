# This file contains builtin players
import subprocess

from player import Player

# This player plays files using mplayer
class mPlayer(Player):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Player.__init__(self)
		
		# VARS
		self.process = None # The Popen process running mplayer
		
	# PLAY -------------------------------------------------------------
	# Play the item
	def play(self, item):
		# Start mplayer
		self.process = subprocess.Popen(self.getArgs(item), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	# STOP -------------------------------------------------------------
	# Kills the mplayer process
	def stop(self):
		if self.process != None:
			self.process.kill()
		
	# GET ARGS ---------------------------------------------------------
	# Gets the arguments to send to mplayer
	def getArgs(self, item):
		# Lets start with this
		args = ["mplayer"]
		
		# Some options
		args.append("-framedrop")
		args.append("-fs")
		args.append("-idx")
		
		# The file we are playing
		args.append(item.path)
		
		# K, should be good.
		return args
		
	# GET --------------------------------------------------------------
	# Get information running process
	def get(self, key):
		if key == 'playing':
			if self.process != None:
				if self.process.poll() == None:
					return True
				else:
					return False
			else:
				return False
