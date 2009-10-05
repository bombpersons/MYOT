# This class describes what the scheduler should do at the
# Start, Middle and End of the time. 
#
# You can use this to make only a selection of shows play during a time,
# Or make only make new episodes play at a certain time of the day.

import os

import settings
from helpers import listDirs, listFiles

from object import Object
from series import Series
from video import Video

class Block(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
		# VARS
		self.series = [] # List of series to play. 
		self.exclude_series = [] # List of series to exclude. If none, then none will be excluded.
		
		self.new_episodes = False # Only play new episodes.
		self.old_episodes = False # Only play old episodes.
		
		self.groups = [] # Only play from these groups
		self.exclude_groups = [] # Don't play any from these groups.
		
		self.use_ads = False # Play ads
		self.ads = [] # List of ads
		self.exclude_ads = [] # 
		
		self.ad_groups = [] # Play only ads from these groups
		self.ad_exclude_groups = [] # Don't play any ads from these groups.
		
		self.picker = settings.PICKER # The picker to use in this block.
		self.ad_picker = settings.AD_PICKER # Thi picker to use to pick adverts
		
	# ONCHOOSE
	# This is run when the schedular picks a show. Overide this to add 
	# your own code.
	def onChoose(self, schedular):
		pass

	# AUTO -------------------------------------------------------------
	# Automatically add series from a folder
	def auto(self, dir):
		#List all dirs
		dirs = listDirs(os.path.join(settings.MEDIA_DIR, dir))
		
		for d in dirs[:]:
			series = Series()
			series.auto(d)
			
			# Check if auto found any files
			if len(series.videos) != 0:
				self.series.append(series)
			
			else:
				dirs.remove(d)
			
	# AUTO AD ----------------------------------------------------------
	# Automatically ad adverts
	def autoAd(self, dir):
		# Find all files in the dir
		files = listFiles(os.path.join(settings.MEDIA_DIR, dir))
		
		# Now sort the files alphabetically
		files.sort()
		
		# Get rid of files that don't have a media extension
		temp = []
		for file in files:
			found = False
			for extension in settings.SERIES_AUTOFIND_EXTENSIONS:
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
			print newVideo.path
			newVideo.number = files.index(file)
			self.ads.append(newVideo)
	
