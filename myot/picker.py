# This class contains code to pick a show. It is intended to be inherited
# from and pluged into a manager instance.

from object import Object

class Picker(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
	# PICK -------------------------------------------------------------
	# The scheduler or manager will pass all the series it wants to pick
	# from. 
	#
	# This function should be overriden, otherwise it will do nothing.
	def pick(self, block):
		pass
		
	# PICK AD ----------------------------------------------------------
	# This function picks an advert
	def pickAd(self, block):
		pass
		
	# SAVE -------------------------------------------------------------
	# Saves the information about series. (Info from last pick)
	def save(self, block):
		for s in self.series:
			if self.picked in s.videos:
				s.pickle.since = 0
			else:
				s.pickle.since += 1
			
			if not block.old_episodes:
				if s.pickle.episode >= s.pickle.num:
					s.pickle.episode = 0
				else:
					s.pickle.episode += 1
		
			s.save()
	
	# GET SERIES
	# This function obtains all the series described in a block and gets
	# the episodes from them.
	def getSeries(self, block):
		# Make a list of series with only the series described in the block.
		finalSeries = []
		
		# Add series
		for series in block.series:
			finalSeries.append(series)
			
		# Remove series
		for series in block.exclude_series:
			finalSeries.remove(series)
			
		#Reload these series
		for series in finalSeries:
			series.auto(series.path)	
		
		# Pick the series from groups
		if block.groups:
			for series in finalSeries[:]:
				if series.group not in block.groups:
					finalSeries.remove(series)
		
		# Remove series from groups
		if block.exclude_groups:
			for series in finalSeries[:]:
				if series.group in block.exclude_group:
					finalSeries.remove(series)
					
		# If only old episodes is true, remove all new episodes
		if block.old_episodes:
			for series in finalSeries[:]:
				for video in series.videos[:]:
					if video.number > series.pickle.episode:
						finalSeries[finalSeries.index(series)].videos.remove(video)
		
		# Ok now return the list
		return finalSeries
			
