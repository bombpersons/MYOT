# This file contains builtin players
import subprocess, os, signal

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
		self.process = subprocess.Popen(self.getArgs(item))
	
	# STOP -------------------------------------------------------------
	# Kills the mplayer process
	def stop(self):
		if self.process != None:
			os.kill(self.process.pid, signal.SIGTERM)

	# GET ARGS ---------------------------------------------------------
	# Gets the arguments to send to mplayer
	def getArgs(self, item):
		# Lets start with this
		args = ["mplayer"]
		
		# Some options
		args.append("-framedrop")
		args.append("-fs")
		args.append("-idx")
		
		# If there are subs for this item, then make mplayer use them
		if item.sub_path != "":
			args.append("-subcp")
			args.append("utf-8")
			
			args.append("-sub")
			args.append(item.sub_path)
		
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
