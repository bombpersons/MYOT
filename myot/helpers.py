# This file contains helpers functions for the other classes.

import os

# LIST FILES -----------------------------------------------------------
# This function lists all the files in a directory (ignoring folders)
def listFiles(dir):
	files = []
	
	for file in os.listdir(dir):
		if os.path.isfile(os.path.join(dir,file)):
			files.append(file)
	
	return files

# LIST DIRS ------------------------------------------------------------
# This function lists all the folders in a folder (ignoring files)
def listDirs(dir):
	files = []
	
	for file in os.listdir(dir):
		if os.path.isdir(os.path.join(dir,file)):
			files.append(file)
	
	return files
