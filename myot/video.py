# Each instance of this class is a video.
# Most managers will automatically create these from folders.

from object import ItemObject

class Video(ItemObject):
	# INIT -------------------------------------------------------------
	def __init__(self):
		ItemObject.__init__(self)
	
