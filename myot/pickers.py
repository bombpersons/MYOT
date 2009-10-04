import settings
from picker import Picker

import random

# A dummy picker
class DummyPicker(Picker):
	def pick(self, block):
		self.series = self.getSeries(block)
		
		self.picked = self.series[0].videos[self.series[0].pickle.episode - 1]
		
		return self.series[0].videos[self.series[0].pickle.episode - 1]

# A random picker. It will keep track of episode numbers, etc.
class RandomPicker(Picker):
	def pick(self, block):
		# Pick a series at random.
		self.series = self.getSeries(block)
		
		print self.series[0].videos
		
		#Seed the ranomizer
		random.seed()
		
		#Now pick a series
		series = random.choice(self.series)
		
		#Now pick an episode
		if block.old_episodes:
			choice = range(0, len(series.videos) - 1)
			if len(choice) == 0:
				choice = [0]
			
			self.picked = series.videos[random.choice(choice)]
			
		else:
			self.picked = series.videos[series.pickle.episode - 1]
		return self.picked

# A class to pick a single new episode from one series.
class LatestEpisodePicker(Picker):
	def pick(self, block):
		# Grab series
		self.series = self.getSeries(block)
		
		# Pick a series at random (we should only have one, but...)
		random.seed()
		series = random.choice(self.series)
		
		# Now choose the latest episode
		self.picked = series.videos[len(series.videos) - 1]
		return self.picked
