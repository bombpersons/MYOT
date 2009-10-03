# This class contains code to pick a show. It is intended to be inherited
# from and pluged into a manager instance.

from object import Object

class Picker(Object):
	# INIT -------------------------------------------------------------
	def __init__(self):
		Object.__init__(self)
		
	# PICK -------------------------------------------------------------
	# Takes the manager as an argument so that this method can access
	# every thing in the manager.
	#
	# This function should be overriden, otherwise it will do nothing.
	def pick(self, manager):
		pass
