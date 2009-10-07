import time

# This a base object that everything should inherit from.
class Object:
	# INIT -------------------------------------------------------------
	def __init__(self):
		# OBJECT WIDE VARIABLES
		self.name = "" # The objects name. 
		self.create_time = time.localtime() # The time this object was created
		
		

# This class is a base class for program item like objects (programs and
# adverts)
class ItemObject(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
		# VARIABLES
		self.path = "" # The full path to the item
		self.sub_path = "" # The full path to subs for this item
		self.groups = [] # Groups that this object is a member of.
		self.number = 0 # The number of this object (e.g order in a series)
