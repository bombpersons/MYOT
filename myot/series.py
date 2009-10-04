import os, pickle

import settings
from helpers import listFiles

from object import Object
from video import Video

# This class contains settings to pickle for a series.
class SeriesPickle(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
		# VARS
		self.episode = 0 # The last episode played.
		self.since = 0 # How many times it's been since this series was last played.
		self.num = 0 # The amount of items in this series.
		

# This class contains many video instances to represent a series.
class Series(Object):
	# INIT -------------------------------------------------------------
	def __init__(self, auto=""):
		# Call inherited __init__'s
		Object.__init__(self)
		
		# Vars
		self.videos = [] # A list of all the videos in this series.
		self.extensions = settings.SERIES_AUTOFIND_EXTENSIONS
		
		self.path = "" # The path to folder containing the series.
		
		self.pickle = SeriesPickle() # The object to save settings to.
		
		# Call auto if a path is passed to us.
		if auto != "":
			self.auto(auto)
		
	# AUTO -------------------------------------------------------------
	# Automatically scan a directory and populate videos.
	def auto(self, dir):
		# Find all files in the dir
		files = listFiles(dir)
		
		# Now sort the files alphabetically
		files.sort()

		# Check for pickle file
		temp = files
		for file in files:
			# Check if this file is the pickle file.
			if file == ".pickle":
				# Load this file
				self.pickle = pickle.load(open(os.path.join(dir, ".pickle"), "rb"))
				temp.remove(file)
		files = temp
		
		# Get rid of files that don't have a media extension
		temp = []
		for file in files:
			found = False
			for extension in self.extensions:
				if file.endswith("." + extension):
					found = True
			if found:
				temp.append(file)
		files = temp
		
		
		# Now make video objects for remaining files
		self.videos = []
		for file in files:
			newVideo = Video()
			newVideo.path = os.path.join(dir, file)
			newVideo.number = files.index(file)
			self.videos.append(newVideo)
			
		# Make this dir our new path
		self.path = dir
		
		# Make sure we note how many files there were.
		self.pickle.num = len(self.videos)
	
	# SAVE -------------------------------------------------------------
	# remembers data in a pickle file
	def save(self):
		pickle.dump(self.pickle, open(os.path.join(self.path, ".pickle"), "wb"))
